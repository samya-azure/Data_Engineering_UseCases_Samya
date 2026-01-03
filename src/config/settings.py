from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "sales.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "sales_processed.csv"
OUTPUT_DATA_PATH = BASE_DIR / "data" / "output" / "sales_summary.csv"
