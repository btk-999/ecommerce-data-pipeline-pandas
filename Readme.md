# E-Commerce Data Pipeline using Pandas

## Project Overview
This project is a modular ETL data pipeline built using Python and Pandas.

The pipeline performs:
- Data ingestion
- Data merging
- Filtering
- Data cleaning
- Currency transformation (USD to INR)
- Aggregations and calculations
- CSV output generation

## Tech Stack
- Python
- Pandas
- OS Module

## Project Structure

ecommerce-data-pipeline-pandas/
│
├── ingest.py
├── merge.py
├── filtering.py
├── clean.py
├── transform.py
├── calc.py
├── savefile.py
├── main.py
└── config.py
```

## Business Logic
- Filters selected product categories
- Filters yearly transactional data
- Converts USD values into INR
- Calculates customer-wise total revenue
- Saves transformed output into CSV

## How to Run

cmd: python main.py

## Future Improvements
- PySpark Migration
