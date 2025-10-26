from src.scraper import run_scraper
from src.data_cleaning import clean_data

def run_etl():
    print(" Starting ETL Pipeline ...")
    run_scraper()
    clean_data()
    print(" ETL Pipeline completed successfully.")
