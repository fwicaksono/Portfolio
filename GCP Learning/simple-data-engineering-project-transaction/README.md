# Project Overview
We will simulate a transactional dataset, store it in Google Cloud Storage (GCS), process it using BigQuery, and create a dashboard using Google Data Studio (Looker Studio).

## Tech Stack
- **Data Generation:** Python
- **Storage:** Google Cloud Storage (GCS)
- **Processing & Querying:** BigQuery
- **Visualization:** Google Data Studio (Looker Studio)

## Project Workflow
1. **Generate Sample Transaction Data**
   - Use Python to generate and save transactional data in CSV format.

2. **Upload Data to Google Cloud Storage (GCS)**
   - Store the generated CSV file in a GCS bucket.

3. **Load Data into BigQuery**
   - Create an external table from the CSV in GCS or load it as a native BigQuery table.

4. **Process Data in BigQuery**
   - Run queries to analyze transaction data, such as total revenue per customer.

5. **Visualize in Google Data Studio**
   - Connect BigQuery data to Looker Studio and create dashboards for insights.

## Installation & Setup
### Prerequisites
- Google Cloud Platform (GCP) account
- Google Cloud SDK installed
- BigQuery and Cloud Storage enabled
- Python installed

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/data-engineering-gcp.git
   cd data-engineering-gcp
   ```

2. **Generate Sample Data**
   ```bash
   python generate_data.py
   ```

3. **Upload to GCS**
   ```bash
   gsutil cp transactions.csv gs://your-bucket-name/
   ```

4. **Create BigQuery Table**
   ```sql
   CREATE OR REPLACE EXTERNAL TABLE `your_project.dataset.transactions`
   OPTIONS (
     format = 'CSV',
     uris = ['gs://your-bucket-name/transactions.csv'],
     skip_leading_rows = 1
   );
   ```

5. **Run Queries in BigQuery**
   ```sql
   SELECT customer_id, COUNT(order_id) AS total_orders, SUM(amount) AS total_spent
   FROM `your_project.dataset.transactions`
   GROUP BY customer_id
   ORDER BY total_spent DESC;
   ```

6. **Create Dashboard in Google Data Studio**
   - Connect to BigQuery
   - Create visualizations for insights

## Conclusion
This project provides a simple end-to-end data engineering pipeline using Google Cloud Platform. Modify and expand it based on your use case. 🚀

