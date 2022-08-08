from kafka import KafkaConsumer
from json import loads
from datetime import datetime
import pandas as pd

class OrderbookConsumer():

    def __init__(self):

        self.consumer = KafkaConsumer(
        'prices',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-id',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

        self._data = dict(orderbook=pd.DataFrame(), ticker=pd.DataFrame())

    def parse(self):
        for data in self.consumer:
            event = data.value
            timestamp = datetime.fromtimestamp(event['params']['data']['timestamp']/1000)
            bids = event['params']['data']['bids']
            asks = event['params']['data']['asks']

            total_bids = 0
            total_asks = 0

            for bid, ask in zip(bids, asks):
                total_bids += bid[1]
                total_asks += ask[1]
            
            mid_price = (bids[0][0] + asks[0][0])/2
            net_ofi = (total_bids - total_asks)/(total_bids + total_asks)
            data = dict(timestamp=[timestamp], mid_price=[mid_price], net_ofi=[net_ofi])

            orderbook = pd.DataFrame(data)
            orderbook.set_index('timestamp')

            self._data['orderbook'] = pd.concat([self._data['orderbook'], orderbook], ignore_index=True, copy=False)
            print(self._data['orderbook'])
            #self._data = pd.merge_asof(self._data, orderbook, on='timestamp')
            
            #instrument = event['params']['data']['instrument_name']

if __name__ == '__main__':

    consumer = OrderbookConsumer()
    consumer.parse()