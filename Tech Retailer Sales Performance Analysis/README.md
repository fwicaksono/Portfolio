# README: TechMart Sales Performance Analysis

---

## **Business Context**
TechMart is a leading tech retailer that sells smartphones, tablets, laptops, and accessories from globally recognized brands such as **Apple**, **Samsung**, **Dell**, **HP**, **Lenovo**, **Google**, **Microsoft**, **Asus**, **Acer**, and **Sony**. The company operates both online and in physical stores across multiple regions, including North America, Europe, Asia, South America, and Africa. Recently, TechMart has observed a decline in overall sales and profitability. To address this, the management has initiated a data-driven project to analyze sales performance, identify trends, and uncover actionable insights to improve business outcomes.

---

## **Problem Statement**
TechMart needs to analyze its sales data to:
1. Identify trends in sales performance across product categories, brands, and regions.
2. Determine the profitability of each product and brand.
3. Understand customer behavior and preferences.
4. Optimize inventory management and pricing strategies.
5. Evaluate the effectiveness of promotions and discounts.

The goal is to provide actionable insights that will help TechMart boost sales, improve profitability, and enhance customer satisfaction.

---

## **Key Insights to Derive**
1. **Sales Trends**: How have sales of smartphones, tablets, and laptops changed over the past year?
2. **Product Performance**: Which brands and products are the most/least profitable?
3. **Regional Analysis**: Which regions are underperforming, and why?
4. **Customer Segmentation**: Who are the most valuable customers, and what are their preferences?
5. **Promotion Impact**: How effective are discounts and promotions in driving sales?

---

## **Dataset Design**
To address the problem, a **multi-table dataset** has been created, which includes the following tables:

1. **Sales Transactions**:
   - `TransactionID`: Unique ID for each transaction.
   - `ProductID`: ID of the product sold.
   - `CustomerID`: ID of the customer.
   - `Region`: Region where the sale occurred.
   - `Date`: Date of the transaction.
   - `Quantity`: Number of units sold.
   - `Price`: Selling price per unit.
   - `Discount`: Discount applied (0, 10%, or 20%).
   - `Promotion`: Promotion applied (if any).

2. **Product Information**:
   - `ProductID`: Unique ID for each product.
   - `ProductName`: Name of the product (e.g., "iPhone 14 Pro", "Galaxy S23 Ultra").
   - `Brand`: Brand of the product.
   - `Category`: Category of the product (Smartphone, Tablet, Laptop).
   - `CostPrice`: Cost price of the product.

3. **Customer Information**:
   - `CustomerID`: Unique ID for each customer.
   - `CustomerName`: Name of the customer.
   - `Region`: Region where the customer is located.
   - `Segment`: Customer segment (Individual, Business, Education).

4. **Regional Data**:
   - `Region`: Name of the region.
   - `Population (M)`: Population in millions.
   - `GDP per Capita (USD)`: Average GDP per capita.

5. **Promotions**:
   - `PromotionID`: Unique ID for each promotion.
   - `PromotionName`: Name of the promotion.
   - `StartDate`: Start date of the promotion.
   - `EndDate`: End date of the promotion.

---

## **Dataset Description**
The dataset consists of the following tables:

### **Sales Transactions**
| TransactionID | ProductID | CustomerID | Region       | Date       | Quantity | Price  | Discount | Promotion     |
|---------------|-----------|------------|--------------|------------|----------|--------|----------|---------------|
| 1             | 1001      | 2001       | North America| 2023-01-15 | 2        | 999.99 | 0.1      | 10% Off       |
| 2             | 1002      | 2002       | Europe       | 2023-03-22 | 1        | 799.99 | 0.0      | None          |

### **Product Info**
| ProductID | ProductName      | Brand   | Category   | CostPrice |
|-----------|------------------|---------|------------|-----------|
| 1001      | iPhone 14 Pro    | Apple   | Smartphone | 900.00    |
| 1002      | Galaxy S23 Ultra | Samsung | Smartphone | 950.00    |

### **Customer Info**
| CustomerID | CustomerName | Region       | Segment   |
|------------|--------------|--------------|-----------|
| 2001       | Customer 2001| North America| Individual|
| 2002       | Customer 2002| Europe       | Business  |

### **Regional Data**
| Region       | Population (M) | GDP per Capita (USD) |
|--------------|----------------|----------------------|
| North America| 350.00         | 55000.00             |
| Europe       | 450.00         | 40000.00             |

### **Promotions**
| PromotionID | PromotionName   | StartDate  | EndDate    |
|-------------|-----------------|------------|------------|
| 1           | 10% Off         | 2023-01-01 | 2023-03-31 |
| 2           | 20% Off         | 2023-04-01 | 2023-06-30 |

