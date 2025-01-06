import os
import subprocess
import sys

def setup_environment():
    print("Starting environment setup...")
    
    # Create virtual environment
    subprocess.run([sys.executable, '-m', 'venv', 'trading_env'])
    print("Virtual environment created")

    # Activate virtual environment
    if os.name == 'nt':  # Windows
        activate_script = os.path.join('trading_env', 'Scripts', 'activate.bat')
    else:  # Unix/Linux/Mac
        activate_script = os.path.join('trading_env', 'bin', 'activate')
    
    # Install required packages
    packages = [
        'pandas',
        'numpy',
        'scikit-learn',
        'yfinance',
        'ta',
        'streamlit',
        'fastapi',
        'uvicorn',
        'pymongo',
        'psycopg2-binary',
        'transformers',
        'python-binance',
        'alpha_vantage'
    ]
    
    print("Installing required packages...")
    for package in packages:
        subprocess.run([sys.executable, '-m', 'pip', 'install', package])
    
    print("Setup completed successfully!")

if __name__ == "__main__":
    setup_environment()
