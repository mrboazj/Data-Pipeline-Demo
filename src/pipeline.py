from pathlib import Path
from ingest import load_transactions
from validate import clean_transactions
from transform import add_derived_fields, build_merchant_summary

def run_pipeline() -> None:
    project_root = Path(__file__).resolve().parents[1]
    input_file = project_root / "data" / "transactions_raw.csv"
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    raw_df = load_transactions(input_file)
    clean_df = clean_transactions(raw_df)
    enriched_df = add_derived_fields(clean_df)
    merchant_summary = build_merchant_summary(enriched_df)

    enriched_df.to_csv(output_dir / "transactions_clean.csv", index=False)
    merchant_summary.to_csv(output_dir / "merchant_summary.csv", index=False)

if __name__ == "__main__":
    run_pipeline()
