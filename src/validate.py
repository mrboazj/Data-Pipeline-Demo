import pandas as pd

REQUIRED_COLUMNS = {
    "transaction_id", "merchant_id", "customer_id", "amount",
    "currency", "status", "created_at", "payment_method"
}
VALID_STATUSES = {"successful", "failed", "pending"}

def check_required_columns(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    check_required_columns(df)
    cleaned = df.copy()
    cleaned["amount"] = pd.to_numeric(cleaned["amount"], errors="coerce")
    cleaned["status"] = cleaned["status"].astype(str).str.strip().str.lower()
    cleaned["currency"] = cleaned["currency"].astype(str).str.strip().str.upper()
    cleaned["payment_method"] = cleaned["payment_method"].astype(str).str.strip().str.lower()
    cleaned["created_at"] = pd.to_datetime(cleaned["created_at"], errors="coerce")
    cleaned = cleaned.dropna(subset=["transaction_id", "merchant_id", "customer_id", "amount", "created_at"])
    cleaned = cleaned[cleaned["amount"] > 0]
    cleaned = cleaned[cleaned["status"].isin(VALID_STATUSES)]
    return cleaned.reset_index(drop=True)
