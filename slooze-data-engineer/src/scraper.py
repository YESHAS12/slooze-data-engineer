import json
import os

OUTPUT_PATH = "data/raw/products_raw.json"

def run_scraper():
    print(" Loading mock data ...")
    if not os.path.exists(OUTPUT_PATH):
        print(" Mock data not found. Please create products_raw.json")
        return 0

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)

    print(f" Loaded {len(products)} products from mock data")
    return len(products)

if __name__ == "__main__":
    run_scraper()
