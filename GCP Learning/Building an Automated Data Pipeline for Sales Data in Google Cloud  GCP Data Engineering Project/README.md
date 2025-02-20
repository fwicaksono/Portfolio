# Google Cloud Data Analytics Project  

This repository contains the code and configuration files for a Google Cloud Data Analytics project. It showcases how to integrate multiple GCP services to build an automated and efficient data pipeline for sales data. This project covers the following key aspects:  

> 📌 **Refer to the YouTube video for a detailed walkthrough of this project.**  

## Overview  

1. **Web Portal**: A Python Flask-based web application that enables users to upload sales data files.  
2. **Storage**: Uploaded files are securely stored in a Google Cloud Storage (GCS) bucket.  
3. **Cloud Function**: Automatically triggers upon file upload to the GCS bucket, processes the data, and loads it into BigQuery.  
4. **ETL Process**: Implements an Extract, Transform, and Load (ETL) workflow to ensure smooth data processing from raw upload to a structured format.  
5. **Reporting**: Provides interactive dashboards and summary views in Looker Studio, featuring key metrics, filtering, and drill-down capabilities.  

## Techstacks

## Architecture  

The project follows a structured architecture integrating web applications, cloud storage, serverless functions, and data visualization tools to streamline the sales data analysis process.  
