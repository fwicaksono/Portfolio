# **Adidas Sales Data Engineering Pipeline**

## **Project Description**
This project builds an end-to-end data engineering pipeline to process Adidas sales data. The pipeline automates data ingestion, transformation, storage, and visualization for analytical insights. The dataset consists of sales transactions from multiple regions, containing retailer details, product information, sales amounts, and profit margins.

The goal is to extract raw sales data, clean and transform it, store it in a structured database, and visualize key business metrics using Power BI. The project leverages cloud-based services for scalability, automation, and monitoring.

## **Tech Stack & Services Used**
- **Storage:** Amazon S3 (Raw data storage)  
- **Compute & Processing:** AWS Glue (ETL), AWS Lambda (automation)  
- **Database:** Amazon RDS (PostgreSQL)  
- **Orchestration:** AWS Step Functions  
- **Visualization:** Power BI (connected to Amazon RDS)  
- **Monitoring:** AWS CloudWatch  

## **Pipeline Workflow**
1. **Data Ingestion:** Sales data (CSV) is uploaded to Amazon S3.
2. **ETL Processing:** AWS Glue extracts and transforms the data, handling cleaning and formatting.
3. **Storage:** Transformed data is loaded into Amazon RDS (PostgreSQL) for structured querying.
4. **Automation:** AWS Lambda triggers data processing and database updates.
5. **Visualization:** Power BI connects to Amazon RDS to create interactive dashboards for sales analysis.

## **Setup & Deployment**
### **1. Create an S3 Bucket and Upload Data**
- Go to **AWS S3** → **Create Bucket** → Upload `adidas_sales.csv`

### **2. Set Up Amazon RDS (PostgreSQL)**
- Create an **Amazon RDS PostgreSQL** instance.
- Create a database and table schema for Adidas sales data.

### **3. Configure AWS Glue for ETL Processing**
- Create a **Glue Crawler** to infer schema from S3 data.
- Set up an **AWS Glue ETL Job** to clean and transform data.

### **4. Automate the Pipeline with AWS Lambda**
- Create an **AWS Lambda function** to trigger data processing.

### **5. Connect Power BI to Amazon RDS**
- Use **Amazon RDS Endpoint** to establish a connection in Power BI.
- Build interactive dashboards for sales analysis.

## **Key Insights & Analysis**
- **Total Sales by Region**
- **Profit Trends Over Time**
- **Top-Selling Products and Retailers**
- **Sales Performance Analysis**

## **Future Improvements**
- Implement real-time data ingestion using AWS Kinesis.
- Optimize database queries for faster analytics.
- Automate reporting and notifications using AWS SNS.

This project demonstrates real-world data engineering concepts, including data pipeline automation, cloud-based ETL, and database management for analytical reporting in Power BI.