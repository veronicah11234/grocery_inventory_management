from app import insert_products, select_all_products
import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class Products:
    def __init__(self, name, price, quantity, supplier_id):
        def __init__(self, name, batch_number, price, quantity, price_per_piece, category, unit):
            self.name = name.capitalize()  # Capitalize the name
            self.price = float(price)  
            self.quantity = int(quantity)  
            self.price_per_piece = float(price_per_piece)  
            self.supplier_id = category.capitalize() 



    def __str__(self):
                return f"Name: {self.name}, Price: ${self.price}, Quantity: ${self.quantity}, supplier_id: ${self.supplier_id}"
    def save(self):
        insert_products(self.name, self.price, self.quantity, self.supplier_id)
    @classmethod
    def get_all_products(cls):
            products_list = []
            for row in select_all_products():
                products = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                products.id = uuid.uuid4().__hash__()
                products.created_at = row[8]
                products_list.append(products.__dict__)
                            
            return products_list
