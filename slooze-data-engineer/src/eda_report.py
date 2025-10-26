import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

CLEAN_PATH = "data/processed/products_clean.csv"
OUTPUT_DIR = "outputs"

def run_eda():
    if not os.path.exists(CLEAN_PATH):
        logging.warning(" CSV is empty or missing. Skipping EDA.")
        return

    df = pd.read_csv(CLEAN_PATH)

    df.fillna({
        "price": 0,
        "company": "Unknown",
        "location": "Unknown",
        "category": "Uncategorized"
    }, inplace=True)

    df['price_numeric'] = df['price'].replace('[\$,]', '', regex=True)
    df['price_numeric'] = pd.to_numeric(df['price_numeric'], errors='coerce').fillna(0)

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1 Summary statistics
    summary_csv_path = os.path.join(OUTPUT_DIR, "summary_statistics.csv")
    df.describe(include='all').to_csv(summary_csv_path)
    logging.info(f" Summary statistics saved to {summary_csv_path}")

    # 2 Category distribution pie chart
    pie_path = os.path.join(OUTPUT_DIR, "category_distribution.png")
    df['category'].value_counts().plot.pie(
        autopct='%1.1f%%', startangle=90, figsize=(6,6), title="Product Categories"
    )
    plt.ylabel('')
    plt.savefig(pie_path, bbox_inches='tight')
    plt.close()
    logging.info(f" Category pie chart saved to {pie_path}")

    # 3 Products per company (bar chart)
    company_path = os.path.join(OUTPUT_DIR, "products_per_company.png")
    df['company'].value_counts().plot.bar(
        figsize=(10,6), title="Number of Products per Company"
    )
    plt.xlabel("Company")
    plt.ylabel("Number of Products")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(company_path, bbox_inches='tight')
    plt.close()
    logging.info(f" Company bar chart saved to {company_path}")

    # 4 Average price per category (bar plot)
    price_path = os.path.join(OUTPUT_DIR, "price_distribution.png")

  
    logging.info(f"Price range: {df['price_numeric'].min()} - {df['price_numeric'].max()}")
    logging.info(f"Price median: {df['price_numeric'].median()}")
    logging.info(f"Price mean: {df['price_numeric'].mean()}")

   
    df_filtered = df[df['price_numeric'] > 0]

    if df_filtered.empty:
        logging.warning(" No valid price data after filtering zeros.")
    else:
        logging.info("Non-zero price entries per category:")
        logging.info(df_filtered['category'].value_counts())
        logging.info("Price distribution per category:")
        logging.info(df_filtered.groupby('category')['price_numeric'].describe())

        
        avg_prices = df_filtered.groupby('category')['price_numeric'].mean()

      
        num_categories = avg_prices.shape[0]
        plt.figure(figsize=(max(12, num_categories * 2), 8))

        
        avg_prices.plot(kind='bar', color='skyblue')
        plt.title("Average Price per Category", fontsize=16)
        plt.xlabel("Category", fontsize=14)
        plt.ylabel("Average Price", fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)
        plt.ylim(0, 10000)  

        plt.tight_layout()
        plt.savefig(price_path, bbox_inches='tight', dpi=200)
        plt.close()
        logging.info(f" Average price bar plot saved to {price_path}")

    # 5 Products per location (bar chart)
    location_path = os.path.join(OUTPUT_DIR, "products_per_location.png")
    df['location'].value_counts().plot.bar(
        figsize=(10,6), title="Number of Products per Location"
    )
    plt.xlabel("Location")
    plt.ylabel("Number of Products")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(location_path, bbox_inches='tight')
    plt.close()
    logging.info(f" Location bar chart saved to {location_path}")

    logging.info(" EDA completed successfully!")

if __name__ == "__main__":
    run_eda()
