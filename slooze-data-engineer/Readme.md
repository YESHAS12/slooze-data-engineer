# Product Data Analysis Pipeline

A complete pipeline for scraping, cleaning, analyzing, and visualizing product data from various categories.

---

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Overview](#pipeline-overview)
  - [Scraping](#scraping)
  - [Data Cleaning](#data-cleaning)
  - [Exploratory Data Analysis](#exploratory-data-analysis)
- [Outputs](#outputs)
- [Contributing](#contributing)
- [License](#license)

---
## Introduction

This project provides a complete pipeline for handling product data, including:
- Scraping product data (or loading mock data)
- Cleaning and preprocessing the data
- Performing exploratory data analysis (EDA)
- Generating visualizations
---
## Project Structure
project-root/
│
├── data/
│   ├── raw/
│   │   └── products_raw.json       # Raw product data
│   └── processed/
│       └── products_clean.csv      # Cleaned product data
│
├── outputs/                         # Generated visualizations and reports
│   ├── category_distribution.png
│   ├── products_per_company.png
│   ├── price_distribution.png
│   ├── products_per_location.png
│   └── summary_statistics.csv
│
├── src/
│   ├── scraper.py                   # Data scraping/loading script
│   ├── data_cleaning.py             # Data cleaning script
│   ├── eda_report.py                # EDA and visualization script
│   └── etl_pipeline.py             # ETL pipeline script
│
├── run_pipeline.py                  # Main pipeline execution script
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies


## Installation
Install the required packages:
pip install -r requiremnts.txt



Usage
To run the complete pipeline:
python run_pipeline.py
This will execute the entire ETL and EDA process.

Pipeline Overview
Scraping
The scraper.py script loads mock product data from data/raw/products_raw.json. This simulates the data scraping process.

Input: data/raw/products_raw.json
Output: Logs the number of products loaded

Data Cleaning
The data_cleaning.py script cleans the raw product data:

Handles missing values

Converts price ranges to numeric values

Standardizes text fields

Saves cleaned data to data/processed/products_clean.csv


Input: data/raw/products_raw.json
Output: data/processed/products_clean.csv
Exploratory Data Analysis
The eda_report.py script performs EDA and generates visualizations:
Summary statistics
Category distribution pie chart
Number of products per company (bar chart)
Average price per category (bar plot)
Number of products per location (bar chart)
Input: data/processed/products_clean.csv
Output: Visualizations and reports in the outputs/ directory



Outputs
The pipeline generates the following outputs:

Cleaned Data: data/processed/products_clean.csv
Visualizations:

outputs/category_distribution.png: Category distribution pie chart
outputs/products_per_company.png: Number of products per company
outputs/price_distribution.png: Average price per category
outputs/products_per_location.png: Number of products per location


Summary Statistics: outputs/summary_statistics.csv


Pipeline Execution
The run_pipeline.py script orchestrates the entire process:

ETL Pipeline: Loads and cleans the data
EDA: Performs exploratory data analysis and generates visualizations

To run the complete pipeline:
python run_pipeline.py
