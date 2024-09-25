import ccxt
import pandas as pd

class DeribitAPI:
    def __init__(self):
        self.exchange = ccxt.deribit()

    def get_instrument_data(self, symbol):
        try:
            return self.exchange.fetch_ticker(symbol)
        except Exception as e:
            print(f"Error fetching instrument data: {e}")
            return None

    def get_historical_data(self, symbol, timeframe='1h', since=None, limit=1000):
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe, since, limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df.set_index('timestamp')
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return pd.DataFrame()

    # Add more methods as needed for order placement, account info, etc.