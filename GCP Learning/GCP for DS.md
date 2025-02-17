# GCP Learning Roadmap for Data Scientists

This roadmap provides a detailed guide to learning Google Cloud Platform (GCP) for data science, including step-by-step mini-projects and a final capstone project to practice each skill.

---

## Table of Contents
1. [Core GCP Services for Data Science](#core-gcp-services-for-data-science)
   - [Google Cloud Storage (GCS)](#google-cloud-storage-gcs)
   - [BigQuery](#bigquery)
2. [Data Processing and Transformation](#data-processing-and-transformation)
   - [Cloud Dataflow](#cloud-dataflow)
   - [Dataproc](#dataproc)
3. [Machine Learning and AI Services](#machine-learning-and-ai-services)
   - [Vertex AI](#vertex-ai)
   - [BigQuery ML](#bigquery-ml)
4. [Data Visualization and Reporting](#data-visualization-and-reporting)
   - [Looker](#looker)
   - [Google Data Studio](#google-data-studio)
5. [Programming and Tools](#programming-and-tools)
   - [Python and SQL](#python-and-sql)
   - [Jupyter Notebooks](#jupyter-notebooks)
6. [DevOps and Deployment](#devops-and-deployment)
   - [Cloud Functions](#cloud-functions)
   - [Cloud Run](#cloud-run)
7. [Security and Access Control](#security-and-access-control)
   - [IAM](#iam)
8. [Monitoring and Logging](#monitoring-and-logging)
   - [Cloud Monitoring](#cloud-monitoring)
9. [Final Capstone Project](#final-capstone-project)

---

## Core GCP Services for Data Science

### Google Cloud Storage (GCS)
- **What to Learn:**
  - Creating buckets and uploading files.
  - Setting access controls (IAM permissions).
  - Using the `google-cloud-storage` Python library.
- **Mini Project: Upload and Analyze a Dataset**
  - Steps:
    1. Create a GCS bucket.
    2. Upload a dataset (e.g., [Titanic dataset](https://www.kaggle.com/c/titanic/data)) to the bucket.
    3. Use Python to download the dataset from GCS and load it into a Pandas DataFrame.
    4. Perform basic data analysis (e.g., summary statistics, missing values).

---

### BigQuery
- **What to Learn:**
  - Writing SQL queries.
  - Loading data from GCS into BigQuery.
  - Using BigQuery ML for machine learning.
- **Mini Project: Analyze NYC Taxi Data**
  - Steps:
    1. Load the [NYC Taxi dataset](https://cloud.google.com/bigquery/public-data) into BigQuery.
    2. Write SQL queries to:
       - Find the average trip distance.
       - Identify the most common pickup locations.
    3. Use BigQuery ML to build a linear regression model predicting trip duration.

---

## Data Processing and Transformation

### Cloud Dataflow
- **What to Learn:**
  - Building ETL pipelines using Apache Beam.
  - Processing streaming data.
- **Mini Project: Process Log Data**
  - Steps:
    1. Create a sample log file (e.g., web server logs).
    2. Write a Dataflow pipeline to:
       - Read the log file from GCS.
       - Extract relevant fields (e.g., timestamp, IP address).
       - Write the processed data to BigQuery.
    3. Run the pipeline and verify the results in BigQuery.

---

### Dataproc
- **What to Learn:**
  - Setting up a Dataproc cluster.
  - Running PySpark jobs.
- **Mini Project: Analyze Sales Data with PySpark**
  - Steps:
    1. Create a Dataproc cluster.
    2. Upload a sales dataset (e.g., [Retail Data Analysis](https://www.kaggle.com/c/retail-data-analytics)) to GCS.
    3. Write a PySpark script to:
       - Calculate total sales by product.
       - Identify the top-selling products.
    4. Run the script on the Dataproc cluster.

---

## Machine Learning and AI Services

### Vertex AI
- **What to Learn:**
  - Using AutoML for automated model training.
  - Training custom models.
  - Deploying models as APIs.
- **Mini Project: Predict House Prices**
  - Steps:
    1. Upload the [California Housing dataset](https://www.kaggle.com/camnugent/california-housing-prices) to Vertex AI.
    2. Use AutoML to train a regression model predicting house prices.
    3. Deploy the model and make predictions via an API.

---

### BigQuery ML
- **What to Learn:**
  - Creating and evaluating models using SQL.
- **Mini Project: Customer Segmentation**
  - Steps:
    1. Load a customer dataset (e.g., [Mall Customer Segmentation](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)) into BigQuery.
    2. Use BigQuery ML to create a k-means clustering model.
    3. Analyze the clusters to identify customer segments.

---

## Data Visualization and Reporting

### Looker
- **What to Learn:**
  - Creating dashboards and visualizations.
  - Writing LookML for data modeling.
- **Mini Project: Sales Dashboard**
  - Steps:
    1. Connect Looker to a sales dataset in BigQuery.
    2. Create a dashboard showing:
       - Total sales over time.
       - Sales by region.
       - Top-selling products.

---

### Google Data Studio
- **What to Learn:**
  - Creating interactive reports.
- **Mini Project: COVID-19 Report**
  - Steps:
    1. Connect Data Studio to a COVID-19 dataset in BigQuery.
    2. Create a report showing:
       - Total cases and deaths by country.
       - Trends over time.

---

## Programming and Tools

### Python and SQL
- **Mini Project: Analyze Movie Ratings**
  - Steps:
    1. Load the [MovieLens dataset](https://grouplens.org/datasets/movielens/) into BigQuery.
    2. Write SQL queries to:
       - Find the highest-rated movies.
       - Calculate average ratings by genre.
    3. Use Python to visualize the results (e.g., bar charts, scatter plots).

---

### Jupyter Notebooks
- **Mini Project: Exploratory Data Analysis (EDA)**
  - Steps:
    1. Use Vertex AI Workbench to create a Jupyter notebook.
    2. Load a dataset (e.g., Iris dataset) and perform EDA:
       - Summary statistics.
       - Visualizations (e.g., pair plots, histograms).
    3. Train a simple machine learning model (e.g., logistic regression).

---

## DevOps and Deployment

### Cloud Functions
- **Mini Project: Automate Data Preprocessing**
  - Steps:
    1. Write a Cloud Function to:
       - Trigger when a new file is uploaded to GCS.
       - Preprocess the file (e.g., clean data, remove duplicates).
       - Save the processed file to another GCS bucket.
    2. Test the function by uploading a sample file.

---

### Cloud Run
- **Mini Project: Deploy a Model API**
  - Steps:
    1. Train a Scikit-learn model (e.g., Iris classification).
    2. Deploy the model as a REST API using Cloud Run.
    3. Test the API by sending sample data and receiving predictions.

---

## Security and Access Control

### IAM
- **Mini Project: Secure a GCS Bucket**
  - Steps:
    1. Create a GCS bucket and upload a dataset.
    2. Set IAM permissions to allow only specific users to access the bucket.
    3. Test access by logging in with different accounts.

---

## Monitoring and Logging

### Cloud Monitoring
- **Mini Project: Monitor a Data Pipeline**
  - Steps:
    1. Set up a Dataflow pipeline.
    2. Use Cloud Monitoring to:
       - Track pipeline performance.
       - Set up alerts for errors.
    3. Analyze logs to debug any issues.

---

## Final Capstone Project

### **Project Name: End-to-End Customer Churn Prediction Pipeline**
- **Objective:** Build a complete data science pipeline to predict customer churn using GCP services.
- **Steps:**

#### 1. **Data Ingestion**
   - Upload a customer dataset (e.g., [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)) to Google Cloud Storage (GCS).

#### 2. **Data Preprocessing**
   - Use **Cloud Dataflow** to:
     - Clean the dataset (e.g., handle missing values, encode categorical variables).
     - Split the data into training and testing sets.
     - Save the processed data to BigQuery.

#### 3. **Data Analysis**
   - Use **BigQuery** to:
     - Perform exploratory data analysis (EDA) using SQL queries.
     - Identify key factors contributing to customer churn.

#### 4. **Model Training**
   - Use **Vertex AI** to:
     - Train a classification model (e.g., XGBoost or Random Forest) to predict churn.
     - Evaluate the model using metrics like accuracy, precision, and recall.

#### 5. **Model Deployment**
   - Deploy the trained model as a REST API using **Cloud Run**.
   - Test the API by sending sample customer data and receiving churn predictions.

#### 6. **Visualization**
   - Use **Looker** or **Google Data Studio** to:
     - Create a dashboard showing churn predictions and key insights (e.g., churn rate by region, top reasons for churn).

#### 7. **Monitoring**
   - Use **Cloud Monitoring** to:
     - Track the performance of the deployed model.
     - Set up alerts for any issues (e.g., high latency, errors in predictions).

#### 8. **Automation**
   - Use **Cloud Functions** to:
     - Automate the retraining of the model when new data is uploaded to GCS.

---

## Resources
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
- [Coursera: Google Cloud Data Engineering](https://www.coursera.org/professional-certificates/google-cloud-data-engineering)
- [Google Cloud Documentation](https://cloud.google.com/docs)
- [YouTube: Google Cloud Channel](https://www.youtube.com/googlecloud)

---

By completing these mini-projects and the capstone, you’ll gain hands-on experience with GCP and build a strong portfolio for data science roles.