import sqlite3

CONN = sqlite3.connect("grocery_inventory.db") 
CURSOR = CONN.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grocery_inventory.db'