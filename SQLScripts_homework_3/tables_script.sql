-- Таблица Customers
CREATE TABLE Customers (
 customer_id INT PRIMARY KEY,
 first_name VARCHAR(50),
 last_name VARCHAR(50),
 age INT,
 country VARCHAR(50)
);
-- Таблица Orders
CREATE TABLE Orders (
 order_id INT PRIMARY KEY,
 item VARCHAR(50),
 amount INT,
 customer_id INT REFERENCES Customers(customer_id)
);
-- Таблица Shippings
CREATE TABLE Shippings (
 shipping_id INT PRIMARY KEY,
 status VARCHAR(20),
 customer INT REFERENCES Customers(customer_id)
);
-- Вставка данных
INSERT INTO Customers (customer_id, first_name, last_name, age, country) VALUES
(1, 'John', 'Doe', 31, 'USA'),
(2, 'Robert', 'Luna', 22, 'USA'),
(3, 'David', 'Robinson', 22, 'UK'),
(4, 'John', 'Reinhardt', 25, 'UK'),
(5, 'Betty', 'Doe', 28, 'UAE'),
(6, 'Alice', 'Smith', 35, 'USA'),
(7, 'Michael', 'Brown', 40, 'UK'),
(8, 'Sarah', 'Davis', 29, 'UAE'),
(9, 'Tom', 'White', 31, 'USA'),
(10, 'Emma', 'Green', 27, 'UK');
INSERT INTO Orders (order_id, item, amount, customer_id) VALUES
(1, 'Keyboard', 400, 4),
(2, 'Mouse', 300, 4),
(3, 'Monitor', 12000, 3),
(4, 'Keyboard', 400, 1),
(5, 'Mousepad', 250, 2),
(6, 'Monitor', 10000, 6),
(7, 'Keyboard', 450, 6),
(8, 'Mouse', 350, 7),
(9, 'Monitor', 11000, 9),
(10, 'Mousepad', 300, 10);
INSERT INTO Shippings (shipping_id, status, customer) VALUES
(1, 'Pending', 2),
(2, 'Pending', 4),
(3, 'Delivered', 3),
(4, 'Pending', 5),
(5, 'Delivered', 1),
(6, 'Delivered', 6),
(7, 'Pending', 7),
(8, 'Delivered', 9),
(9, 'Pending', 8),
(10, 'Delivered', 10);