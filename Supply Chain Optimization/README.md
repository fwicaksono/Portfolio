# Supply Chain Optimization: TechMart Electronics

## Project Description
This project aims to optimize the supply chain of **TechMart Electronics**, a company specializing in selling electronic products such as laptops, smartphones, and tablets. The provided dataset includes information on product demand, inventory, supplier costs, lead times, and storage costs.

## Problem Statement
TechMart Electronics faces several challenges in its supply chain management:

1. **Suboptimal Inventory Levels:**  
   - Sometimes, products run out of stock before new orders arrive (stockout), leading to lost sales.  
   - On the other hand, excessive stock results in high storage costs.  

2. **High Operational Costs:**  
   - Poorly managed ordering and storage costs reduce profit margins.  

3. **Uncertain Demand:**  
   - Product demand fluctuates monthly, making production and procurement planning difficult.  

4. **Variable Lead Times:**  
   - Supplier lead times vary, making it difficult to predict when stock will arrive.  

### **Objectives**  
TechMart Electronics aims to optimize its supply chain by:  
1. Determining the **optimal order quantity** for each product.  
2. Minimizing **total operational costs** (ordering cost + storage cost).  
3. Ensuring **stock availability** to meet customer demand.  
4. Improving **overall supply chain efficiency**.  

## Dataset  
The dataset consists of **1,000 rows** and includes the following columns:  

| **Column**        | **Description**                                                       |
|-------------------|-----------------------------------------------------------------------|
| **Product_ID**    | Unique ID for each product.                                         |
| **Product_Name**  | Product name (Laptop, Smartphone, Tablet).                          |
| **Category**      | Product category (Electronics).                                     |
| **Demand**        | Monthly product demand.                                             |
| **Inventory**     | Current stock availability.                                         |
| **Supplier_ID**   | Supplier ID.                                                        |
| **Supplier_Name** | Supplier name.                                                      |
| **Supplier_Cost** | Cost per unit from the supplier.                                    |
| **Lead_Time**     | Supplier delivery time (in days).                                   |
| **Holding_Cost**  | Storage cost per unit per month.                                   |
| **Order_Cost**    | Fixed ordering cost per order.                                     |
| **Date**          | Date of data recording.                                            |

### **Sample Data**
| Product_ID | Product_Name | Category    | Demand | Inventory | Supplier_ID | Supplier_Name             | Supplier_Cost | Lead_Time | Holding_Cost | Order_Cost | Date       |
|------------|-------------|-------------|--------|-----------|-------------|---------------------------|---------------|-----------|--------------|------------|------------|
| P123       | Laptop      | Electronics | 200    | 50        | S001        | GlobalTech Supplies       | 500           | 7         | 10           | 100        | 2023-03-15 |
| P456       | Smartphone  | Electronics | 150    | 30        | S002        | ElectroWorld Distributors | 300           | 5         | 8            | 100        | 2023-05-20 |
| P789       | Tablet      | Electronics | 100    | 20        | S003        | GadgetHub Inc.            | 200           | 10        | 5            | 100        | 2023-07-10 |

## **Analysis Questions**
1. What is the **optimal order quantity (EOQ)** for each product?  
2. What is the **total cost** for each product?  
3. How does **lead time** affect inventory levels?  
4. Are there any **seasonal demand patterns** that can be identified?  
5. How can inventory levels be optimized to avoid stockouts and excess stock?  

## **Key Performance Indicators (KPIs)**
1. **Economic Order Quantity (EOQ):**  
   Optimal order quantity for each product.  

2. **Total Cost:**  
   Ordering cost + storage cost.  

3. **Service Level:**  
   Percentage of customer demand met without stockouts.  

4. **Inventory Turnover Ratio:**  
   How quickly inventory is sold and replenished.  

5. **Lead Time Variability:**  
   Variation in supplier delivery times.  

## **How to Use the Dataset**
1. **Calculate EOQ (Economic Order Quantity):**  
   Use the `Demand`, `Holding_Cost`, and `Order_Cost` columns to compute EOQ.  

2. **Calculate Total Cost:**  
   Use the `Demand`, `EOQ`, `Holding_Cost`, and `Order_Cost` columns to determine total costs.  

3. **Analyze Lead Time:**  
   Use the `Lead_Time` column to ensure stockout situations are minimized.  

4. **Visualize Data:**  
   Use libraries such as `matplotlib` or `seaborn` to visualize relationships between different features.

