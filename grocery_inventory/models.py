# INSERT INTO sales (product_id, quantity_sold, sale_date, revenue_generated) 
# VALUES (1, 10, '2024-03-21', 50.00);
# .mode column
# .headers on

# SELECT * FROM products;
# SELECT * FROM suppliers;
# SELECT * FROM sales;
# SELECT * FROM purchases;
# DELETE FROM products WHERE product_id = 1;
# DELETE FROM products;
# DELETE FROM sales;
# DELETE FROM purchases;
# DELETE FROM suppliers;
# INSERT INTO products (name, price, quantity_in_stock, supplier_id) 
# VALUES ('Apple', 1.99, 100, 1);
# INSERT INTO suppliers (name, contact_info)
# VALUES ('Supplier Name', 'Contact Information');
# INSERT INTO purchases (product_id, supplier_id, quantity, purchase_date, total_cost)
# VALUES (1, 1, 10, '2024-03-21', 50.00);
# ALTER TABLE purchases
# ADD CONSTRAINT fk_product
# FOREIGN KEY (product_id)
# REFERENCES products(product_id);ALTER TABLE products
# ADD CONSTRAINT fk_supplier
# FOREIGN KEY (supplier_id)
# REFERENCES suppliers(supplier_id);