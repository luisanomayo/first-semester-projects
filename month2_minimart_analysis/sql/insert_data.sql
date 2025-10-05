-- SQL script to insert sample data
INSERT INTO customers (customer_id, name, email, join_date) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com', '2023-02-15'),
(2, 'Brian Smith', 'brian.smith@example.com', '2023-03-20'),
(3, 'Cynthia Lee', 'cynthia.lee@example.com', '2023-05-11'),
(4, 'Daniel Perez', 'daniel.perez@example.com', '2023-06-08'),
(5, 'Emma Brown', 'emma.brown@example.com', '2023-07-19');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1, 'Wireless Mouse', 'Electronics', 24.99),
(2, 'Laptop Stand', 'Accessories', 42.50),
(3, 'Coffee Mug', 'Kitchen', 9.99),
(4, 'Notebook (A5)', 'Stationery', 5.25),
(5, 'Bluetooth Headphones', 'Electronics', 79.00),
(6, 'Water Bottle', 'Fitness', 15.49),
(7, 'Yoga Mat', 'Fitness', 25.00),
(8, 'Mechanical Keyboard', 'Electronics', 99.00),
(9, 'Portable Charger', 'Electronics', 35.75),
(10, 'Desk Lamp', 'Home Decor', 28.50);

INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES
(1, 1, 3, 2, '2023-03-01'),
(2, 1, 1, 1, '2023-03-15'),
(3, 2, 2, 1, '2023-04-05'),
(4, 2, 5, 1, '2023-04-10'),
(5, 3, 4, 3, '2023-06-02'),
(6, 3, 3, 1, '2023-06-05'),
(7, 3, 7, 1, '2023-06-10'),
(8, 4, 1, 1, '2023-07-01'),
(9, 4, 9, 2, '2023-07-08'),
(10, 4, 10, 1, '2023-07-15'),
(11, 5, 5, 1, '2023-08-03'),
(12, 5, 2, 1, '2023-08-05'),
(13, 5, 8, 1, '2023-08-09'),
(14, 1, 9, 1, '2023-08-15'),
(15, 2, 6, 2, '2023-08-21'),
(16, 3, 10, 1, '2023-09-01'),
(17, 4, 4, 4, '2023-09-03'),
(18, 5, 7, 1, '2023-09-06'),
(19, 2, 3, 2, '2023-09-09'),
(20, 1, 8, 1, '2023-09-15');
