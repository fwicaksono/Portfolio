SELECT * FROM pizza_sales

1. Total Revenue :

SELECT SUM(total_price) AS total_revenue 
FROM pizza_sales


2. Average order spending :

SELECT (SUM(total_price) / COUNT(DISTINCT(order_id))) AS AOS 
FROM pizza_sales


3. Total Pizza Sold:
SELECT SUM(quantity) AS total_pizza_sold
FROM pizza_sales

4. Total Number Orders:
SELECT COUNT(DISTINCT(order_id)) as total_orders 
FROM pizza_sales

5. Average Pizza Per order
WITH pizza_sold AS (
    SELECT SUM(quantity) AS total_pizza_sold
    FROM pizza_sales
),
total_order AS (
    SELECT COUNT(DISTINCT order_id) AS total_orders
    FROM pizza_sales
)
SELECT 
    (pizza_sold.total_pizza_sold / total_order.total_orders) AS avg_per_order
FROM 
    pizza_sold, total_order;

6. Daily Trend For Orders:

SELECT TO_CHAR(order_date, 'Day') AS order_day, 
       COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY TO_CHAR(order_date, 'Day'), EXTRACT(DOW FROM order_date)
ORDER BY EXTRACT(DOW FROM order_date);

7. Monthly Trend For Orders:

SELECT TO_CHAR(order_date, 'Mon') AS order_month, 
       COUNT(DISTINCT order_id) AS total_orders
FROM pizza_sales
GROUP BY order_month, EXTRACT(MONTH FROM order_date)
ORDER BY EXTRACT(MONTH FROM order_date), order_month;

8. % of Sales by Pizza Category

SELECT pizza_category, SUM(quantity) as Total_Quantity_Sold
FROM pizza_sales
GROUP BY pizza_category
ORDER BY Total_Quantity_Sold DESC


8. % of Sales by Pizza Size

SELECT pizza_size, CAST(SUM(total_price) AS DECIMAL(10,2)) as total_revenue,
CAST(SUM(total_price) * 100 / (SELECT SUM(total_price) from pizza_sales) AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_size
ORDER BY pizza_size


10 Top 5 Best Sellers by Revenue, Total Quantity and Total Orders

TOP 5 By Revenue

SELECT pizza_name, SUM(total_price) AS Total_Revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue DESC
LIMIT 5;

BOTTOM 5 By Revenue
SELECT pizza_name, SUM(total_price) AS Total_Revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue ASC
LIMIT 5;

TOP 5 BY QUANTITY
SELECT pizza_name, SUM(quantity) AS Total_Pizza_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizza_Sold DESC
LIMIT 5;

BOTTOM 5 BY QUANTITY
SELECT pizza_name, SUM(quantity) AS Total_Pizza_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizza_Sold ASC
LIMIT 5;







