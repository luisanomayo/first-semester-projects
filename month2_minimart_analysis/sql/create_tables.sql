-- Active: 1749329170628@@127.0.0.1@5432@altschool_db
-- SQL script to create necessary tables
CREATE TABLE IF NOT EXISTS customers(
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR (100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    join_date  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR (50) NOT NULL,
    category VARCHAR(25) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);


ALTER TABLE customers
ALTER COLUMN join_date TYPE DATE;