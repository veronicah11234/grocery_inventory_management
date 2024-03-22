from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from category import Category
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.supplier_id'))  

    supplier = relationship("Suppliers", back_populates="products") 
    sales = relationship("Sales", back_populates="product")  
    purchases = relationship("Purchases", back_populates="product")

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity_in_stock={self.quantity_in_stock}, supplier_id={self.supplier_id})"

    def save(self):
        insert_products(self.name, self.price, self.quantity, self.supplier_id)

    def save(self):
        insert_products(self.name, self.price, self.quantity_in_stock, self.supplier_id)

    @staticmethod
    def get_all_products():
        return Product.query.all()
    
class Suppliers(db.Model):
    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.Integer, nullable=False)

    products = relationship("Product", back_populates="supplier")
    purchases = relationship("Purchases", back_populates="supplier")  # Ensure this line is correctly added

    def __repr__(self):
        return f"Suppliers(name='{self.name}', contact_info={self.contact_info})"
    
    def save(self):
        insert_supplier(self.name, self.contact_info)

    @staticmethod
    def get_all_suppliers():
        return Suppliers.query.all()


class Sales(db.Model):
    sale_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))  
    quantity_sold = db.Column(db.Integer)
    sale_date = db.Column(db.Date)
    revenue_generated = db.Column(db.Float)

    product = relationship("Product", back_populates="sales")

    def __repr__(self):
        return f"Sales(sale_id ='{self.sale_id }',product_id={self.product_id}, quantity_sold={self.quantity_sold}, sale_date={self.sale_date}, revenue_generated={self.revenue_generated})"

class Purchases(db.Model):
    purchase_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, db.ForeignKey('product.id'))  
    supplier_id = Column(Integer, db.ForeignKey('suppliers.supplier_id'))  
    quantity = Column(Integer)
    purchase_date = Column(Date)
    total_cost = Column(Float)

    product = relationship("Product", back_populates="purchases") 
    supplier = relationship("Suppliers", back_populates="purchases")

    def __repr__(self):
        return f"Purchases(purchase_id='{self.purchase_id}', product_id={self.product_id}, supplier_id={self.supplier_id}, quantity={self.quantity}, purchase_date={self.purchase_date}, total_cost={self.total_cost})"

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    output = []
    for product in products:
        product_data = {'name': product.name, 'price': product.price}
        output.append(product_data)
    return jsonify({'products': output})

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], quantity_in_stock=data['quantity'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'})


@app.route('/purchases', methods=['GET'])
def get_purchases():
    purchases = Purchases.query.all()
    output = []
    for purchase in purchases:
        purchase_data = {'purchase_id': purchase.purchase_id, 'product_id': purchase.product_id, 'supplier_id': purchase.supplier_id, 'quantity': purchase.quantity, 'purchase_date': purchase.purchase_date.strftime("%Y-%m-%d"), 'total_cost': purchase.total_cost}
        output.append(purchase_data)
    return jsonify({'purchases': output})

@app.route('/suppliers', methods=['POST'])
def add_supplier():
    data = request.get_json()
    new_supplier = Suppliers(name=data['name'], contact_info=data['contact_info'])
    with app.app_context():
        db.session.add(new_supplier)
        db.session.commit()
    return jsonify({'message': 'Supplier added successfully'})


@app.route('/sales', methods=['GET'])
def get_sales():
    sales = Sales.query.all()
    output = []
    for sale in sales:
        sale_data = {'sale_id': sale.sale_id, 'product_id': sale.product_id, 'quantity_sold': sale.quantity_sold, 'sale_date': sale.sale_date.strftime("%Y-%m-%d"), 'revenue_generated': sale.revenue_generated}
        output.append(sale_data)
    return jsonify({'sales': output})

@app.route('/sales', methods=['POST'])
def add_sale():
    data = request.get_json()
    new_sale = Sales(product_id=data['product_id'], quantity_sold=data['quantity_sold'], sale_date=data['sale_date'], revenue_generated=data['revenue_generated'])
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale added successfully'})

@staticmethod
def get_all_supplier():
    return Suppliers.query.all()

def insert_products(name, price, quantity, supplier_id):
    with app.app_context():
        new_product = Product(name=name, price=price, quantity_in_stock=quantity, supplier_id=supplier_id)
        db.session.add(new_product)
        db.session.commit()

def insert_supplier(name, contact_info):
    with app.app_context():
        new_supplier = Suppliers(name=name, contact_info=contact_info)
        db.session.add(new_supplier)
        db.session.commit()



def select_all_products():
    products = Product.query.all()
    return products

if __name__ == '__main__':
    app.run(debug=True)
