# 🍕 Pizza Sales Analysis

## 📌 Project Overview
This project focuses on analyzing pizza sales data. The data, originally stored in a CSV file, is migrated to a **PostgreSQL database** for structured storage. The analysis is conducted using **SQL queries** to generate insights before visualizing the results in **Power BI**.

## 📂 Dataset
The dataset contains the following columns:

| Column Name         | Description |
|---------------------|-------------|
| `pizza_id`         | Unique identifier for each pizza |
| `order_id`         | Unique identifier for each order |
| `pizza_name_id`    | Unique identifier for each pizza name |
| `quantity`         | Number of pizzas ordered |
| `order_date`       | Date of the order |
| `order_time`       | Time of the order |
| `unit_price`       | Price per unit of pizza |
| `total_price`      | Total price for the order |
| `pizza_size`       | Size of the pizza (Small, Medium, Large, etc.) |
| `pizza_category`   | Category of the pizza (Vegetarian, Classic, etc.) |
| `pizza_ingredients` | List of ingredients used in the pizza |
| `pizza_name`       | Name of the pizza |

## 🛠️ Project Workflow
1. **Data Migration**
   - Load the CSV file into **PostgreSQL** for structured data management.

2. **Data Exploration & Insights with SQL**
   - Perform SQL queries to extract key insights from the data.
   - Examples of insights include:
     - Best-selling pizzas
     - Peak order times
     - Revenue trends
     - Customer preferences

3. **Data Visualization in Power BI**
   - Create interactive dashboards to present findings effectively.
   - Visuals include:
     - Sales trends over time
     - Top-selling pizza categories
     - Revenue by pizza size

## 📊 Technologies Used
- **PostgreSQL** for database storage and SQL queries
- **Power BI** for data visualization
- **SQL** for data transformation and insight generation


## 📌 Future Improvements
- Automate data extraction and transformation.
- Implement advanced analytics such as predictive sales forecasting.
- Integrate real-time data updates.
