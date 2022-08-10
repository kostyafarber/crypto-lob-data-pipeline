from datetime import datetime
import glob
import os

# API labels from Binance
labels_aggTrades = ['Aggregate tradeId', 'Price', 'Quantity', 'First TradeId', 'Last tradeId', 'Timestamp', 'Was the buyer the maker?', 'Was the trade the best price match?']
labels_klines = ["Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset", "Number of Trades", "Taker buy base", "Taker buy Quote", "Ignore"]

# parse dates from Binance CSV (timestamp)
def parse_dates(timestamp: str):
    """
    A date parser which parses timestamps from binance for pandas dataframe.
    """
    return datetime.utcfromtimestamp(int(timestamp)/1000)

data_path = '../data/data/spot/monthly/aggTrades/ETHBTC/*'

files = glob.glob(data_path)

def get_api_keys(client_id, client_secret, aws=False):
    if aws:
        # obtain deribit api keys from aws
        ssm = boto3.client('ssm', region_name='ap-southeast-2')
        response = ssm.get_parameters(Names=[client_id, client_secret], WithDecryption=True)
        client_id = response['Parameters'][0]["Value"]
        client_secret = response['Parameters'][1]["Value"]
        return client_id, client_secret
    else:
        client_id = os.environ[client_id]
        client_secret = os.environ[client_secret]
        return client_id, client_secret


if __name__ == "__main__":
    print(files)