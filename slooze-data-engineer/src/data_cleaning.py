import os
import json
import pandas as pd
import re

RAW_PATH = "data/raw/products_raw.json"
CLEAN_PATH = "data/processed/products_clean.csv"


def parse_price(price_str):
    """Convert price strings like '$3,800 - $4,300' or 'JP¥309 - JP¥771' into average numeric values."""
    if not isinstance(price_str, str) or price_str.strip() == "" or price_str.strip().upper() == "N/A":
        return None

    cleaned = re.sub(r"[^\d\.\-\s]", "", price_str)

    if "-" in cleaned:
        parts = cleaned.split("-")
        try:
            nums = [float(p.strip()) for p in parts if p.strip() != ""]
            return sum(nums) / len(nums)
        except ValueError:
            return None
    else:
        try:
            return float(cleaned.strip())
        except ValueError:
            return None


def clean_data():
    """Clean raw product data and save as processed CSV."""
    if not os.path.exists(RAW_PATH):
        print("⚠️ No raw data found. Exiting clean_data.")
        return


    with open(RAW_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)


    df = pd.DataFrame(data)

    if df.empty:
        print("⚠️ No data found in raw file.")
        return


    df.dropna(subset=["name"], inplace=True)


    df["price_numeric"] = df["price"].apply(parse_price)


    df["company"] = df["company"].fillna("Unknown")
    df["location"] = df["location"].fillna("Unknown")
    df["location"].fillna("Unknown", inplace=True)


    os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)


    df.to_csv(CLEAN_PATH, index=False)
    print(f" Cleaned data saved to {CLEAN_PATH}")


    print(f" Total records after cleaning: {len(df)}")
    print(f" Columns: {list(df.columns)}")


if __name__ == "__main__":
    clean_data()
