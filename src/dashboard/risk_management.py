import streamlit as st

class PositionSizeCalculator:
    def calculate(self, account_size, risk_percentage):
        return account_size * (risk_percentage/100)

class RiskManagementPanel:
    # Your provided code here
