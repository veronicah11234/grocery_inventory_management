from .app import db
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///suppliers.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    supplier = db.relationship('Supplier', backref=db.backref('products', lazy=True))

    @classmethod
    def add_product(cls, name, price, quantity_in_stock, supplier_id):
        new_product = cls(name=name, price=price, quantity_in_stock=quantity_in_stock, supplier_id=supplier_id)
        db.session.add(new_product)
        db.session.commit()

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def suppliers():
    if request.method == 'POST':
        name = request.form['name']
        contact_info = request.form['contact_info']

        new_supplier = Supplier(name=name, contact_info=contact_info)
        db.session.add(new_supplier)
        db.session.commit()

        return 'Supplier added successfully.'

    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)