from src.ingestion.ingest_csv import read_sales_data
from src.transformation.transform_data import transform_sales_data
from src.validation.validate_data import validate_sales_data
from src.loading.load_to_file import save_processed_data, save_summary

def run_sales_etl():
    print("Starting Sales ETL Pipeline")

    df = read_sales_data()
    df = transform_sales_data(df)
    validate_sales_data(df)
    save_processed_data(df)
    save_summary(df)

    print("Sales ETL Pipeline completed successfully")
