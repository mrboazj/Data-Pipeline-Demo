import pandas as pd
from src.validate import clean_transactions

def test_clean_transactions_removes_invalid_amounts():
    df = pd.DataFrame([
        {"transaction_id":"TXN001","merchant_id":"M001","customer_id":"C001","amount":100,"currency":"zar","status":"successful","created_at":"2026-03-01 08:15:00","payment_method":"debit_order"},
        {"transaction_id":"TXN002","merchant_id":"M001","customer_id":"C002","amount":-50,"currency":"zar","status":"failed","created_at":"2026-03-01 08:20:00","payment_method":"debit_order"},
    ])
    cleaned = clean_transactions(df)
    assert len(cleaned) == 1
