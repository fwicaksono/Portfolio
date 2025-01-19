/*
1. Who are the top 5 customers by total spending?
*/
/*
WITH total AS (
	SELECT 
		s.customer_id, p.product_id, (p.price * s.quantity) AS total_spending_per_product
	FROM 
		products p
	JOIN 
		sales s
	ON p.product_id = s.product_id
)

SELECT c.name, SUM(t.total_spending_per_product) AS total_spending
FROM
	customers c
JOIN
	total t
ON 
	c.customer_id = t.customer_id
GROUP BY
	c.customer_id
ORDER BY total_spending DESC
 */
/*
2. What is the average customer lifetime value (CLTV)? */



/*
3. Which region has the most active customers?
4. What are the top 5 products by revenue?
5. Which product categories generate the highest revenue?
6. What is the stock status of products?
7. What is the daily revenue trend?
8. Which regions have the highest sales over time?
9. What is the most popular payment method?
10. Who are the top-performing salespersons by revenue?
11. Which salesperson has the highest average order value?
12. How is salesperson performance distributed across regions?
13. What is the average delivery time for orders?
14. Which regions have the highest stock turnover?
15. What is the reorder frequency of products?
*/