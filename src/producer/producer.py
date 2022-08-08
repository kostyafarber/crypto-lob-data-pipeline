from deribit import DeribitClient
from datetime import datetime
import pandas as pd
import os
import json
from kafka import KafkaProducer

client_id = os.environ["CLIENT_ID_DERIBIT"]
client_secret = os.environ["CLIENT_SECRET_DERIBIT"]

exchange_version = 'wss://www.deribit.com/ws/api/v2/'

class DeribitProducer(DeribitClient):
    def __init__(self, client_id, client_secret, testnet=False) -> None:
        """Generates crpyto data. Can collect and save to csv.

        Args:
            client_id (str): Public API Key
            client_secret (str): Private API Key
            testnet (bool, optional): Whether to use tesnet exchange. Defaults to False.
        """
        
        super().__init__(client_id, client_secret, testnet=testnet)
        self._data = dict(orderbook=pd.DataFrame(), ticker=pd.DataFrame())
        self.producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'])

    def _process_callback(self, response: json):
        """Override this method to process the callback message

        Args:
            response (json): Contains the response message from the websocket.
        """

        # processes LOB data
        if 'params' in response.keys() and response['method'] == 'subscription':
            if response['params']['channel'] == 'book.BTC-PERPETUAL.none.10.100ms':
                
                # send json to kafka topic
                self.producer.send(topic='prices', value=json.dumps(response).encode('utf-8'))
                print("message sent: {}".format(response))

    def _on_open_message(self):

        # To subscribe to this channel:
        msg = \
            {"jsonrpc": "2.0",
            "method": "public/subscribe",
            "id": 42,
            "params": {
                "channels": ['book.BTC-PERPETUAL.none.10.100ms']}
            }
        
        self.ws.send(json.dumps(msg))

if __name__ == '__main__':

    stream = DeribitProducer(client_id, client_secret)
    stream.start()