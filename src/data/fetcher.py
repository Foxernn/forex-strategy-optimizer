import pandas as pd
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
from datetime import datetime, timedelta
from config.config import Config

class ForexDataFetcher:
    def __init__(self):
        self.client = oandapyV20.API(access_token=Config.OANDA_API_KEY)
        
    def fetch_historical_data(self, pair, timeframe, count=5000):
        """Fetch historical forex data from OANDA"""
        try:
            params = {
                "count": count,
                "granularity": timeframe
            }
            
            r = instruments.InstrumentsCandles(instrument=pair,
                                             params=params)
            self.client.request(r)
            
            # Convert to DataFrame
            data = []
            for candle in r.response['candles']:
                if candle['complete']:
                    data.append({
                        'timestamp': pd.to_datetime(candle['time']),
                        'open': float(candle['mid']['o']),
                        'high': float(candle['mid']['h']),
                        'low': float(candle['mid']['l']),
                        'close': float(candle['mid']['c']),
                        'volume': int(candle['volume'])
                    })
            
            df = pd.DataFrame(data)
            df.set_index('timestamp', inplace=True)
            return df
            
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return None
    
    def get_current_price(self, pair):
        """Get current price for a forex pair"""
        try:
            params = {
                "count": 1,
                "granularity": "M1"
            }
            
            r = instruments.InstrumentsCandles(instrument=pair,
                                             params=params)
            self.client.request(r)
            
            return float(r.response['candles'][0]['mid']['c'])
            
        except Exception as e:
            print(f"Error getting current price: {str(e)}")
            return None
