SELECT * FROM adidas_sales

1. Total Sales Per Retailer – Identify which retailer generates the highest revenue.

SELECT retailer, SUM(total_sales) AS revenue FROM adidas_sales
GROUP BY retailer
ORDER BY revenue DESC

2. Best-Selling Product Categories – Find out which products have the highest demand.

SELECT product, SUM(units_sold) as sold FROM adidas_sales
GROUP BY product
ORDER BY sold DESC
 

3. Daily Revenue Trend – Analyze how sales change on a daily basis.
SELECT DATE(Invoice_Date) AS Sales_Date, SUM(units_sold) AS Daily_Revenue
FROM adidas_sales
GROUP BY Sales_Date
ORDER BY Sales_Date;


4. Most Profitable State – Determine which states contribute the most profit.
SELECT state, SUM(operating_profit) AS NET_PROFIT , SUM(units_sold) AS SOLD FROM adidas_sales
GROUP BY state
ORDER BY NET_PROFIT DESC

5. Top-Selling Cities – Identify the cities with the highest total revenue.
SELECT state, SUM(units_sold) AS UNIT_SOLD , SUM(total_sales) AS REVENUE FROM adidas_sales
GROUP BY state
ORDER BY REVENUE DESC

6. Average Profit Margin Per Product – Understand which products yield the highest profitability.
SELECT product, AVG(operating_margin) AS AVG_MARG, SUM(total_sales) AS TOTAL_REV, SUM(operating_profit) AS TOTAL_PROF FROM adidas_sales
GROUP BY product
ORDER BY AVG_MARG DESC

7. In-Store vs. Online Sales Comparison – Compare revenue generated from different sales methods.
SELECT sales_method, SUM(total_sales) AS TOTAL_REV, SUM(units_sold) AS UNIT_SOLD FROM adidas_sales
GROUP BY sales_method
ORDER BY UNIT_SOLD DESC

8. Revenue Growth Over Time – Track monthly revenue trends.

SELECT 
    TO_CHAR(Invoice_Date, 'Month YYYY') AS Sales_Month, 
    SUM(units_sold) AS Monthly_Units_Sold,
    SUM(total_sales) AS Monthly_Revenue
FROM adidas_sales
GROUP BY Sales_Month
ORDER BY MIN(Invoice_Date);

