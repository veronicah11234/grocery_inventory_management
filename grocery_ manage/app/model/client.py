from app.model import Product, Supplier

# Add a new product
def add_product(name, price, quantity_in_stock, supplier_id):
    Product.add_product(name, price, quantity_in_stock, supplier_id)
    print('Product added successfully')

# Get all products
def get_products():
    products = Product.get_all_products()
    print('Products:')
    for product in products:
     print(product)
     return Product.query.all()

# Add a new supplier
def add_supplier(name, contact_info):
    Supplier.add_supplier(name, contact_info)
    print('Supplier added successfully')

# Get all suppliers
def get_suppliers():
    suppliers = Supplier.get_all_suppliers()
    print('Suppliers:')
    for supplier in suppliers:
        print(supplier)
        return Supplier.query.all()


if __name__ == '__main__':
    add_product('Apple', 1.99, 100, 1)
    add_product('Banana', 0.99, 150, 1)
    get_products()
    add_supplier('Fresh Farms', 'contact@freshfarms.com')
    get_suppliers()
