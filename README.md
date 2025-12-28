# Vendor Sales Performance & Inventory Optimization Analysis

## Overview
This project analyzes vendor sales performance, profitability, procurement efficiency, and inventory health using transactional purchase and sales data. The goal is to identify revenue concentration, optimize procurement decisions, detect slow-moving inventory, and support data-driven decision-making through analysis and interactive dashboards.

The workflow covers the complete analytics lifecycle: CSV ingestion → SQLite database → data transformation and feature engineering → exploratory analysis → Power BI visualization.

---

## Business Objectives
- Identify top-performing vendors and brands contributing to sales and gross profit.
- Analyze procurement dependency and purchase concentration across vendors.
- Evaluate the impact of bulk purchasing on unit costs.
- Detect slow-moving inventory and quantify capital locked in unsold stock.
- Highlight high-margin but low-sales products for targeted growth opportunities.

---

## Dataset & Data Pipeline
- Raw datasets are stored as CSV files in the `Datasets/` directory.
- Python scripts ingest CSV files into a SQLite database.
- SQL is used to merge and aggregate transactional tables into a vendor-level summary.
- The final dataset is cleaned, enriched with KPIs, and used for analysis and visualization in Power BI.

---

## Repository Structure

├── Datasets: Raw CSV files used for analysis|

├── ingestion_db.py: Ingests raw CSV files into a SQLite database

├── get_vendor_summary.py: Merges tables, cleans data, and creates the final vendor-level summary

├── Exploratory Data Analysis.ipynb: Initial data exploration, distributions, and statistical insights

├── Vendor-Performance-Analysis.ipynb: Complete analysis including feature engineering and business insights

├── Dashboard.pbix: Interactive Power BI dashboard

├── Dashboard.pdf: PDF export of the Power BI dashboard

└── README.md: Project documentation

---

## Feature Engineering & KPIs
The following metrics were created to support analysis:
- Gross Profit
- Profit Margin
- Stock Turnover
- Sales-to-Purchase Ratio
- Unsold Inventory Value
- Purchase Contribution Percentage

These KPIs enable evaluation of vendor performance, inventory efficiency, and procurement optimization.

---

## Power BI Dashboard
The dashboard is organized into two analytical views:

### Page 1: Vendor Performance & Revenue Overview
- KPIs: Total Sales, Total Purchase, Gross Profit
- Top vendors by sales and gross profit
- Vendor purchase contribution analysis
- Sales vs Profit scatter analysis

### Page 2: Inventory Efficiency & Cost Optimization
- Stock turnover analysis
- Vendors with high unsold inventory value
- Sales-to-purchase efficiency
- High-margin but low-sales products

---

## Key Insights
- Revenue and procurement spend are highly concentrated among a small set of vendors.
- Bulk purchasing significantly reduces unit costs, especially for large order sizes.
- Several vendors exhibit low stock turnover, indicating slow-moving inventory.
- A significant amount of working capital is locked in unsold inventory.
- High-margin but low-sales products represent low-risk growth opportunities.

---

## Limitations
- The analysis is based on historical data and does not account for seasonality or future demand changes.
- Customer-level behavior and promotional impact data were not available.
- Inventory holding costs and vendor contract terms were not included.
- Aggregated metrics may mask product-level or time-specific variations.

---

## Tools & Technologies
- Python (Pandas, NumPy, SQLAlchemy)
- SQLite
- SQL
- Jupyter Notebook
- Power BI

---

## Conclusion
This project demonstrates an end-to-end analytics workflow, from data ingestion and transformation to business insight generation and dashboarding. The findings support improved vendor management, procurement optimization, inventory efficiency, and risk reduction through data-driven decision-making.

---

## How to Run
1. Place raw CSV files inside the `Datasets/` folder.
2. Run `ingestion_db.py` to ingest data into SQLite.
3. Run `get_vendor_summary.py` to generate the final vendor-level summary.
4. Explore analysis using the Jupyter notebooks.
5. Open `Dashboard.pbix` in Power BI Desktop to view the dashboard.
