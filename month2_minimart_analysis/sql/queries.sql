-- SQL queries for retrieving insights

--basic queries: SEECT, WHER, ORDER BY

-- 1. List all customers
SELECT * FROM customers;

-- 2 filter products by category
SELECT * 
FROM products 
WHERE category = 'Electronics';

--3 list recent orders by date (limit 5)
SELECT * 
FROM orders 
ORDER BY order_date DESC LIMIT 5;

--aggregate functions: count, sum, avg

--4. number of total orders
SELECT COUNT(*) AS total_orders 
FROM orders;

--5. revenue per product
SELECT o.product_id, 
        p.product_name, 
        SUM(o.quantity) AS total_quantity, 
        SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY o.product_id, p.product_name;

--6. Average product price
SELECT ROUND(AVG(price),2) AS average_price
FROM products;


-- joins: INNER JOIN, LEFT JOIN

--7. detailed order information (with customer and product details)
SELECT o.order_id, 
       o.order_date, 
       c.name, 
       p.product_name, 
       o.quantity, 
       (o.quantity * p.price) AS total_price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;

--8. List all customers and their orders (including those without orders)
SELECT c.customer_id, 
       c.name, 
       o.order_id, 
       o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

--9. show all products even if they have no orders
SELECT p.product_id, 
       p.product_name, 
       COALESCE (SUM(o.quantity),0) AS total_sold
FROM products p
LEFT JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name
ORDER BY product_id ASC;