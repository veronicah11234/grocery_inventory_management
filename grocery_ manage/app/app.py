from flask import request, redirect, url_for,render_template

from . import app
from .model.app import db
from .model.models import Product, Supplier

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('price'))
        quantity = int(request.form.get('quantity'))
        supplier_id = int(request.form.get('supplier'))

        # Add the product to the database
        new_product = Product(name=name, price=price, quantity_in_stock=quantity, supplier_id=supplier_id)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('products'))  # Redirect to the products page after adding the product
    else:
        # If it's a GET request, simply render the add_product.html template
        return render_template('add_product.html')

@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        name = request.form.get('name')
        contact_info = request.form.get('contact_info')

        # Add the supplier to the database
        new_supplier = Supplier(name=name, contact_info=contact_info)
        db.session.add(new_supplier)
        db.session.commit()

        # Redirect to the suppliers page after adding the supplier
        return redirect(url_for('suppliers'))
    else:
        # If it's a GET request, simply render the add_supplier.html template
        return render_template('add_supplier.html')

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)

@app.route('/suppliers')
def suppliers():
    suppliers = Supplier.query.all()
    return render_template('suppliers.html', suppliers=suppliers)
