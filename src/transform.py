import pandas as pd

def add_derived_fields(df: pd.DataFrame) -> pd.DataFrame:
    transformed = df.copy()
    transformed["transaction_date"] = transformed["created_at"].dt.date
    transformed["is_successful"] = transformed["status"].eq("successful")
    return transformed

def build_merchant_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("merchant_id", as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            total_amount=("amount", "sum"),
            successful_transactions=("is_successful", "sum"),
        )
    )
    summary["success_rate"] = (
        summary["successful_transactions"] / summary["transaction_count"]
    ).round(2)
    return summary.sort_values(by=["success_rate", "total_amount"], ascending=[False, False])
