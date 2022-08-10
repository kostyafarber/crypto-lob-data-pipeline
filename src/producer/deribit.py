import time
import json
import hashlib
import hmac
import os
from websocket import WebSocketApp, enableTrace
from datetime import datetime, timedelta
import pandas as pd
import secrets
import sys
from argparse import ArgumentParser
from threading import Thread

# get api keys
client_id = os.environ["CLIENT_ID_DERIBIT"]
client_secret = os.environ["CLIENT_SECRET_DERIBIT"]

class DeribitClient(Thread, WebSocketApp):
    def __init__(self, client_id, client_secret, testnet=False) -> None:
        """Base client for Deribit apps.

        Args:
            client_id (str): Public API Key
            client_secret (str): Private API Key
            testnet (bool, optional): Whether to use testnet exchange. Defaults to False.
        """

        # housekeeping
        Thread.__init__(self)
        self.client_id = client_id
        self.client_secret = client_secret
        self.testnet = testnet
        self.exchange_version = self._set_exchange()
        self.time = datetime.now()
        self.expires_in = None
        self.heartbeat_requested_flag = 0
        self.heartbeat_set_flag = 0

        # Client Signature Authentication
        self.tstamp = str(int(time.time()) * 1000)
        self.data = ''
        self.nonce = secrets.token_urlsafe(10)
        self.base_signature_string = self.tstamp + "\n" + self.nonce + "\n" + self.data
        self.byte_key = client_secret.encode()
        self.message = self.base_signature_string.encode()
        self.signature = hmac.new(self.byte_key, self.message, hashlib.sha256).hexdigest()

        self.parser = ArgumentParser()
        self.args = self._add_args()
    
    def _set_exchange(self):
        if self.testnet:
            exchange_version = 'wss://test.deribit.com/ws/api/v2'
            return exchange_version
        else:
            exchange_version = 'wss://www.deribit.com/ws/api/v2/'
            return exchange_version

    def _authentication(self):
        # Initial Authentication
        ws_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "public/auth",
            "params": {
                "grant_type": "client_signature",
                "client_id": self.client_id,
                "timestamp": self.tstamp,
                "nonce": self.nonce,
                "signature": self.signature,
                "data": self.data}
        }
        
        self.ws.send(json.dumps(ws_data))

    def _on_message(self, ws, message):
            
        response = json.loads(message)
        
        self._process_callback(response)

        # housekeeping connection tasks
        if 'result' in response.keys(): 

            if response['result']['token_type'] == 'bearer':
                print(f'SUCCESSFULLY CONNECTED AT: {self.time.strftime("%Y-%m-%d %H:%M:%S")}\n')
            
                expires_in = response['result']['expires_in']
                self.expires_in = (self.time + timedelta(seconds=expires_in))
                print(f'AUTHENTICATION EXPIRES IN: {self.expires_in.strftime("%Y-%m-%d %H:%M:%S")}\n')


        # respond to a test request
        if 'params' in response.keys() and response['method'] == 'heartbeat':                                    # noqa: E501
            ws_data = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "public/test",
                "params": {
                }
            }
            self.ws.send(json.dumps(ws_data))
        
        # heartbeat set success check and heartbeat response
        if 'params' in response.keys() and response['params']['type'] == 'heartbeat' and self.heartbeat_set_flag == 0:      # noqa: E501
            self.heartbeat_set_flag = 1
            print('Heartbeat Successfully Initiated at: ' + str(datetime.now().time().strftime('%H:%M:%S'))) 
        
    def _on_open(self, ws):

        self._authentication()

         # Initiating Heartbeat
        if self.heartbeat_set_flag == 0 and self.heartbeat_requested_flag == 0:                                                     # noqa: E501
            self.heartbeat_requested_flag = 1
            print('Heartbeat Requested at: ' + str(datetime.now().time().strftime('%H:%M:%S')))                                     # noqa: E501
            ws_data = {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "public/set_heartbeat",
                        "params": {
                            "interval": 60
                        }
                        }
            self.ws.send(json.dumps(ws_data))

        self._on_open_message()

    def _on_close(self, ws):
        #print('CONNECTION CLOSED AT: ' + str(datetime.now().time().strftime('%H:%M:%S')))  # noqa: E501
        print('Attempting Reconnection at: ' + str(datetime.now().time().strftime('%H:%M:%S')))  # noqa: E501
        self.run()

    def run(self):
        self.ws = WebSocketApp(self.exchange_version, on_message=self._on_message, on_open=self._on_open)
    
        if self.args.trace:
            enableTrace(True)   

        # run forever
        while True:
            try:
                self.ws.run_forever()
            except:
                continue
    
    # override this method to process the websocket response
    def _process_callback(self, response):
        pass

    def _on_open_message(self):
        pass

    def _add_args(self):

        self.parser.add_argument('--trace', type=bool)
        self.parser.add_argument('--testnet', type=bool)
        args = self.parser.parse_args()

        return args
        

if __name__ == '__main__':

    test = DeribitClient(client_id, client_secret, testnet=True)
    test.start()
