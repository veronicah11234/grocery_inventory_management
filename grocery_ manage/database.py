from config import CONN, CURSOR
# Function to create database and tables
def create_product_table():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity_in_stock INTEGER,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        )
    ''')
    CONN.commit()
    # Create Suppliers table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INTEGER PRIMARY KEY,
            name TEXT,
            contact_info TEXT
        )
    ''')
    CONN.commit()

    # Create Purchases table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            supplier_id INTEGER,
            quantity INTEGER,
            purchase_date DATE,
            total_cost REAL,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        )
    ''')
    CONN.commit()
    # Create Sales table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY,
            product_id INTEGER,
            quantity_sold INTEGER,
            sale_date DATE,
            revenue_generated REAL,
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    CONN.commit()
#     conn.commit()
#     conn.close()

# # Call the function to create the database
# create_database()
