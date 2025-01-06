import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Trading Pairs
    FOREX_PAIRS = ["EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF"]
    
    # Timeframes
    TIMEFRAMES = {
        "M1": 60,        # 1 minute
        "M5": 300,       # 5 minutes
        "M15": 900,      # 15 minutes
        "H1": 3600,      # 1 hour
        "H4": 14400,     # 4 hours
        "D": 86400,      # 1 day
    }
    
    # Default Settings
    DEFAULT_TIMEFRAME = "H1"
    DEFAULT_PAIR = "EUR_USD"
    
    # Risk Management
    MAX_POSITION_SIZE = 100000
    RISK_PER_TRADE = 0.02  # 2% risk per trade
    MAX_DRAWDOWN = 0.10    # 10% maximum drawdown
    
    # API Credentials (to be set in .env file)
    OANDA_API_KEY = os.getenv('OANDA_API_KEY')
    OANDA_ACCOUNT_ID = os.getenv('OANDA_ACCOUNT_ID')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///trading_bot.db')
    
    # Logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "logs/trading_bot.log"
