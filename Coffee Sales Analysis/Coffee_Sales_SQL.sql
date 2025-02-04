SELECT * FROM coffee_sales

1. What is the total revenue generated from coffee sales?
SELECT SUM(money) AS total_revenue FROM coffee_sales 

2. How many transactions were made using cash versus card?
SELECT cash_type, COUNT(cash_type) FROM coffee_sales
GROUP BY cash_type

3. What are the top 5 best-selling coffee types?
SELECT coffee_name, COUNT(coffee_name) AS sold FROM coffee_sales
GROUP BY coffee_name
ORDER BY sold DESC

4. What is the average amount spent per transaction?
SELECT ROUND(AVG(money), 2) AS average_trans FROM coffee_sales 

5. What are the peak sales hours in a day?
SELECT 
    EXTRACT(HOUR FROM datetime) AS hour_of_day,
    COUNT(*) AS total_sales
FROM coffee_sales
GROUP BY hour_of_day
ORDER BY total_sales DESC


6. Which day of the week has the highest sales?
SELECT 
	TO_CHAR(c.date, 'Day') AS day_of_week, COUNT(*) AS sold
FROM coffee_sales c
GROUP BY day_of_week
ORDER BY sold DESC

7. Which coffee type generates the highest revenue?

SELECT SUM(money) AS revenue, coffee_name FROM coffee_sales
GROUP BY coffee_name
ORDER BY revenue desc

7. What percentage of transactions are cash versus card payments?

WITH total_trans AS (
    SELECT COUNT(cash_type) AS total 
	FROM coffee_sales
)
SELECT c.cash_type, COUNT(c.cash_type)* 100.0 /t.total AS percentage
FROM coffee_sales c
JOIN total_trans t ON 1=1
GROUP BY c.cash_type, t.total;

