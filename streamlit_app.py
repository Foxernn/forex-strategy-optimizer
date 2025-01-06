import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

class DashboardState:
    def __init__(self):
        if 'data' not in st.session_state:
            st.session_state.data = None
        if 'last_update' not in st.session_state:
            st.session_state.last_update = None
        if 'metrics' not in st.session_state:
            st.session_state.metrics = None

def create_sample_data(timeframe, pair):
    intervals = {
        "1m": "T",
        "5m": "5T",
        "15m": "15T",
        "1h": "H",
        "4h": "4H",
        "1d": "D"
    }
    
    dates = pd.date_range(
        start='2025-01-01', 
        end='2025-01-05', 
        freq=intervals[timeframe]
    )
    
    base_prices = {
        "EUR/USD": 1.2000,
        "GBP/USD": 1.5000,
        "USD/JPY": 110.00,
        "USD/CHF": 0.9000
    }
    
    base_price = base_prices[pair]
    volatility = 0.0002 if timeframe in ["1m", "5m"] else 0.002
    
    data = pd.DataFrame({
        'timestamp': dates,
        'price': np.random.normal(base_price, volatility, len(dates)),
        'volume': np.random.randint(1000, 5000, len(dates))
    })
    return data

def update_metrics(data, ma_fast, ma_slow):
    data['MA_fast'] = data['price'].rolling(window=ma_fast).mean()
    data['MA_slow'] = data['price'].rolling(window=ma_slow).mean()
    
    win_rate = np.random.uniform(0.45, 0.75)
    profit_factor = np.random.uniform(1.1, 2.0)
    sharpe = np.random.uniform(1.0, 2.5)
    max_drawdown = np.random.uniform(0.05, 0.15)
    
    return {
        'win_rate': f"{win_rate:.2%}",
        'profit_factor': f"{profit_factor:.2f}",
        'sharpe': f"{sharpe:.2f}",
        'max_drawdown': f"{max_drawdown:.2%}",
        'trades': int(len(data) * 0.1),
        'avg_win_loss': f"{np.random.uniform(1.2, 1.8):.2f}"
    }

def main():
    st.set_page_config(
        page_title="Forex Trading Strategy Optimizer",
        page_icon="📈",
        layout="wide"
    )
    
    dashboard_state = DashboardState()

    st.title("📊 Forex Trading Strategy Optimizer")
    
    with st.sidebar:
        st.header("Strategy Settings")
        
        pair = st.selectbox(
            "Select Currency Pair",
            ["EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF"]
        )
        
        timeframe = st.selectbox(
            "Select Timeframe",
            ["1m", "5m", "15m", "1h", "4h", "1d"]
        )
        
        st.subheader("Strategy Parameters")
        
        ma_fast = st.slider("Fast MA Period", 5, 50, 10)
        ma_slow = st.slider("Slow MA Period", 20, 200, 50)
        risk_percent = st.slider("Risk per Trade (%)", 0.1, 5.0, 1.0)
        
        if st.button("Run Analysis"):
            st.session_state.data = create_sample_data(timeframe, pair)
            st.session_state.last_update = datetime.now()
            st.session_state.metrics = update_metrics(st.session_state.data, ma_fast, ma_slow)

    if st.session_state.data is not None:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Price Chart")
            fig = go.Figure()
            
            fig.add_trace(go.Candlestick(
                x=st.session_state.data['timestamp'],
                open=st.session_state.data['price'],
                high=st.session_state.data['price']+0.0002,
                low=st.session_state.data['price']-0.0002,
                close=st.session_state.data['price']
            ))
            
            fig.add_trace(go.Scatter(
                x=st.session_state.data['timestamp'],
                y=st.session_state.data['MA_fast'],
                name=f'MA{ma_fast}',
                line=dict(color='orange')
            ))
            
            fig.add_trace(go.Scatter(
                x=st.session_state.data['timestamp'],
                y=st.session_state.data['MA_slow'],
                name=f'MA{ma_slow}',
                line=dict(color='blue')
            ))
            
            fig.update_layout(
                height=500,
                template="plotly_dark",
                xaxis_rangeslider_visible=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Performance Metrics")
            metrics = st.session_state.metrics
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Win Rate", metrics['win_rate'])
                st.metric("Profit Factor", metrics['profit_factor'])
                st.metric("Sharpe Ratio", metrics['sharpe'])
            with col2:
                st.metric("Max Drawdown", metrics['max_drawdown'])
                st.metric("Total Trades", metrics['trades'])
                st.metric("Avg Win/Loss", metrics['avg_win_loss'])
    
        st.subheader("Strategy Analysis")
        tab1, tab2, tab3 = st.tabs(["Performance", "Trade List", "Optimization"])
        
        with tab1:
            st.line_chart(st.session_state.data['price'])
        
        with tab2:
            st.dataframe({
                'Date': ['2025-01-01', '2025-01-02', '2025-01-03'],
                'Type': ['Buy', 'Sell', 'Buy'],
                'Entry': [1.2000, 1.2050, 1.1980],
                'Exit': [1.2050, 1.1980, 1.2030],
                'Profit/Loss': ['+$500', '-$700', '+$500']
            })
        
        with tab3:
            st.write("Parameter Optimization Results")
            st.bar_chart(np.random.randn(20, 3))

if __name__ == "__main__":
    main()
