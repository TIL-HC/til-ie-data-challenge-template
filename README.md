# Retail Data Engineering Challenge

## 🏢 The Client Scenario
Your client is a large retail company. They are currently struggling to reconcile their **Sales** data with their **Rebates** data. The Head of Sales is concerned about data quality and needs a reliable view of performance.

They have provided two raw datasets but are unable to match them up accurately to calculate the true net revenue per region.

## 🎯 The Objective
You have been asked to deliver a Proof of Concept (POC) pipeline. 
Your goal is to demonstrate **Databricks Data Engineering best practices** to turn raw files into a reliable data product.

You must:
1.  **Ingest** the raw sales and rebate data.
2.  **Process** the data to handle quality issues and reconcile the datasets.
3.  **Model** the final output for business consumption (e.g., a Star Schema or Dimensional Model).
4.  **Analyze** the data to generate key insights.

## 🛠️ Technical Requirements
* **Language:** Python / PySpark.
* **Storage:** Delta Lake.
* **Architecture:** We expect you to design a pipeline architecture that reflects industry standards for scalability, data quality, and traceability.

## 📂 The Data
The data is hosted at the following URL:
* **URL:** [INSERT_YOUR_S3_URL_HERE]
* **Format:** CSV (Header included)
* **Files included:** `sales_transactions.csv`, `rebate_transactions.csv`

## 📝 Deliverables
You have full autonomy over the project structure. Your submission must include:

### 1. The Pipeline Code (`src/`)
A PySpark pipeline that takes the data from raw source to final analytical tables. 
* We will evaluate your code based on modularity, data quality checks, and how you structure your data flow.

### 2. Analysis Script
A script (e.g., `analysis.py` or `insights.sql`) that queries your final data model to answer:
* Total Sales vs. Total Rebates by Region.
* Top Performing Sales Reps.
* Any data quality issues found (e.g., How many rebates could not be matched to a sale?).

### 3. Presentation
A PDF or Slide Deck (Max 5 slides) addressed to the **Head of Sales**.
* Summarize key insights.
* Highlight data quality issues encountered.
* Explain your architectural choices and why you chose them.

## 🚀 How to Run (Zero Setup)
1.  Click the **Code** button (green) in GitHub.
2.  Select the **Codespaces** tab.
3.  Click **Create codespace on main**.
4.  Wait for the environment to build (approx. 2 mins).
5.  The terminal will open with **PySpark** and **Delta Lake** pre-installed.

### Usage
You can run your python scripts in the terminal:
```bash
python src/your_script_name.py
