# Grocery Sales Database - Data Card

## Overview
The Grocery Sales Database is a structured relational dataset designed for analyzing sales transactions, customer demographics, product details, employee records, and geographical information across multiple cities and countries. This dataset is ideal for data analysts, data scientists, and machine learning practitioners looking to explore sales trends, customer behaviors, and business insights.

## Database Schema
The dataset consists of seven interconnected tables:

| File Name        | Description                                           |
|------------------|-------------------------------------------------------|
| `categories.csv`  | Defines the categories of the products.               |
| `cities.csv`      | Contains city-level geographic data.                  |
| `countries.csv`   | Stores country-related metadata.                      |
| `customers.csv`   | Contains information about the customers who make purchases. |
| `employees.csv`   | Stores details of employees handling sales transactions. |
| `products.csv`    | Stores details about the products being sold.         |
| `sales.csv`       | Contains transactional data for each sale.           |

## Table Descriptions

### 1. categories
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | CategoryID    | INT         | Unique identifier for each product category.         |
|      | CategoryName  | VARCHAR(45) | Name of the product category.                        |

### 2. cities
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | CityID        | INT         | Unique identifier for each city.                     |
|      | CityName      | VARCHAR(45) | Name of the city.                                    |
|      | Zipcode       | DECIMAL(5,0)| Population of the city.                              |
| FK   | CountryID     | INT         | Reference to the corresponding country.              |

### 3. countries
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | CountryID     | INT         | Unique identifier for each country.                  |
|      | CountryName   | VARCHAR(45) | Name of the country.                                 |
|      | CountryCode   | VARCHAR(2)  | Two-letter country code.                             |

### 4. customers
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | CustomerID    | INT         | Unique identifier for each customer.                 |
|      | FirstName     | VARCHAR(45) | First name of the customer.                          |
|      | MiddleInitial | VARCHAR(1)  | Middle initial of the customer.                      |
|      | LastName      | VARCHAR(45) | Last name of the customer.                           |
| FK   | CityID        | INT         | City of the customer.                                |
|      | Address       | VARCHAR(90) | Residential address of the customer.                 |

### 5. employees
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | EmployeeID    | INT         | Unique identifier for each employee.                 |
|      | FirstName     | VARCHAR(45) | First name of the employee.                          |
|      | MiddleInitial | VARCHAR(1)  | Middle initial of the employee.                      |
|      | LastName      | VARCHAR(45) | Last name of the employee.                           |
|      | BirthDate     | DATE        | Date of birth of the employee.                       |
|      | Gender        | VARCHAR(10) | Gender of the employee.                              |
| FK   | CityID        | INT         | Unique identifier for the city.                      |
|      | HireDate      | DATE        | Date when the employee was hired.                    |

### 6. products
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | ProductID     | INT         | Unique identifier for each product.                  |
|      | ProductName   | VARCHAR(45) | Name of the product.                                 |
|      | Price         | DECIMAL(4,0)| Price per unit of the product.                       |
|      | CategoryID    | INT         | Unique category identifier.                          |
|      | Class         | VARCHAR(15) | Classification of the product.                       |
|      | ModifyDate    | DATE        | Last modified date.                                  |
|      | Resistant     | VARCHAR(15) | Product resistance category.                         |
|      | IsAllergic    | VARCHAR     | Indicates whether the item is an allergen.           |
|      | VitalityDays  | DECIMAL(3,0)| Product vitality type classification.                |

### 7. sales
| Key  | Column Name   | Data Type   | Description                                          |
|------|---------------|-------------|------------------------------------------------------|
| PK   | SalesID       | INT         | Unique identifier for each sale.                     |
| FK   | SalesPersonID | INT         | Employee responsible for the sale.                   |
| FK   | CustomerID    | INT         | Customer making the purchase.                        |
| FK   | ProductID     | INT         | Product being sold.                                  |
|      | Quantity      | INT         | Number of units sold.                                |
|      | Discount      | DECIMAL(10,2)| Discount applied to the sale.                        |
|      | TotalPrice    | DECIMAL(10,2)| Final sale price after discounts.                    |
|      | SalesDate     | DATETIME    | Date and time of the sale.                           |
|      | TransactionNumber | VARCHAR(25) | Unique identifier for the transaction.             |

## Use Cases
Despite being a four-month snapshot and existing independently of external data sources, this dataset offers a rich environment for aspiring data scientists to practice and enhance their SQL skills. Here are some approachable and practical use cases:

### 1. Monthly Sales Performance
- **Objective**: Analyze sales performance within the four-month period to identify trends and patterns.
- **Tasks**:
  - Calculate total sales for each month.
  - Compare sales performance across different product categories each month.

### 2. Top Products Identification
- **Objective**: Determine which products are the best and worst performers within the dataset timeframe.
- **Tasks**:
  - Rank products based on total sales revenue.
  - Analyze sales quantity and revenue to identify high-demand products.
  - Examine the impact of product classifications on sales performance.

### 3. Customer Purchase Behavior
- **Objective**: Understand how customers interact with products during the four-month period.
- **Tasks**:
  - Segment customers based on their purchase frequency and total spend.
  - Identify repeat customers versus one-time buyers.
  - Analyze average order value and basket size.

### 4. Salesperson Effectiveness
- **Objective**: Evaluate the performance of sales personnel in driving sales.
- **Tasks**:
  - Calculate total sales attributed to each salesperson.
  - Identify top-performing and underperforming sales staff.
  - Analyze sales trends based on individual salesperson contributions over time.

### 5. Geographical Sales Insights
- **Objective**: Explore how sales are distributed across different cities and countries within the dataset.
- **Tasks**:
  - Map sales data to specific cities and countries to identify high-performing regions.
  - Compare sales volumes between various geographical areas.
  - Assess the effectiveness of regional sales strategies.

## Data Relationships
- **Sales**: Each sale is linked to a Product, Customer, and Employee through their respective IDs. Each sale is linked to a location via the customer.
- **Customers**: Associated with a City and a Country to provide geographic context.
- **Employees**: Manage sales and are uniquely identified by EmployeeID.
- **Products**: Categorized under specific Categories to organize the inventory.
- **Geography**: Cities belong to Countries, offering higher-level geographic segmentation.

## Resources
- [Grocery Sales Dataset on Kaggle](https://www.kaggle.com/datasets/andrexibiza/grocery-sales-dataset)
