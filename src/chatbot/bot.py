class SimpleChatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you with your trading strategies today?",
            "Hi there! Ready to optimize your trading strategies?",
            "Welcome! How can I help you with your trading goals?"
        ]
        self.strategy_responses = {
            "ma": "Moving Average strategy analysis: Fast MA crosses above/below Slow MA generate signals.",
            "risk": "Risk management is crucial. I recommend starting with 1-2% risk per trade.",
            "optimize": "Strategy optimization involves testing different parameter combinations.",
            "backtest": "Backtesting helps validate strategy performance using historical data."
        }

    def get_greeting(self):
        import random
        return random.choice(self.greetings)

    def respond(self, query):
        query = query.lower()
        
        # Strategy related queries
        if "strategy" in query:
            if "ma" in query or "moving average" in query:
                return self.strategy_responses["ma"]
            return "Let me help you analyze your trading strategy. Could you provide more details?"
            
        # Risk management queries
        elif "risk" in query:
            return self.strategy_responses["risk"]
            
        # Optimization queries
        elif "optimize" in query or "optimization" in query:
            return self.strategy_responses["optimize"]
            
        # Backtest queries
        elif "backtest" in query or "testing" in query:
            return self.strategy_responses["backtest"]
            
        # Default response
        else:
            return "I'm here to assist with trading strategies and risk management. Could you clarify your question?"

    def analyze_strategy(self, params):
        return f"Analyzing strategy with parameters: {params}. Looking for optimal entry and exit points."

    def get_risk_advice(self, risk_level="medium"):
        risk_advice = {
            "low": "Conservative approach: 1% risk per trade recommended.",
            "medium": "Balanced approach: 1-2% risk per trade suggested.",
            "high": "Aggressive approach: Up to 3% risk per trade, but not recommended for beginners."
        }
        return risk_advice.get(risk_level, risk_advice["medium"])
