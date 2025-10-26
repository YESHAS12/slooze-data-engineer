from src.etl_pipeline import run_etl
from src.eda_report import run_eda

print(" Slooze Data Engineer Pipeline Starting ...")
run_etl()
run_eda()
print(" All stages (ETL + EDA) executed successfully.")
