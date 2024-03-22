from tabulate import tabulate
from app import Product, Suppliers
from app import app


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all products")
    print("2. See all suppliers")
    print("3. Add product")
    print("4. Add supplier")

def print_products_neat(data):
    rows = [[item.id, item.name, item.price, item.quantity_in_stock, item.supplier_id] for item in data]
    headers = ["ID", "Name", "Price", "Quantity", "Supplier ID"]
    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)

def print_suppliers_neat(data):
    rows = [[supplier.supplier_id, supplier.name, supplier.contact_info] for supplier in data]
    headers = ["ID", "Name", "Contact Info"]
    table = tabulate(rows, headers=headers, tablefmt="pretty")
    print(table)

def print_all_products():
    with app.app_context():
        print("Here are all the products:")
        print_products_neat(Product.query.all())

def print_all_suppliers():
    print("Here are all the suppliers:")
    print_suppliers_neat(Suppliers.query.all())

def get_product_details_from_cli():
    name = input("Enter product name: ").capitalize()
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    supplier_id = int(input("Enter supplier ID: "))
    
    add_product(name, price, quantity, supplier_id)

def get_supplier_details_from_cli():
    name = input("Enter supplier name: ")
    contact_info = input("Enter contact info: ")
    
    add_supplier(name, contact_info)

def add_product(name, price, quantity, supplier_id):
    product = Product(name=name, price=price, quantity_in_stock=quantity, supplier_id=supplier_id)
    product.save()
    print("Product added successfully")

def add_supplier(name, contact_info):
    supplier = Suppliers(name=name, contact_info=contact_info)
    supplier.save()
    print("Supplier added successfully")

def view_all_products():
    products = Product.query.all()
    for product in products:
        print(f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity in Stock: {product.quantity_in_stock}, Supplier ID: {product.supplier_id}")

def view_all_suppliers():
    suppliers = Suppliers.query.all()
    for supplier in suppliers:
        print(f"Supplier ID: {supplier.supplier_id}, Name: {supplier.name}, Contact Info: {supplier.contact_info}")


def exit_program():
    print("Thank you for using the inventory management system.")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "0":
            exit_program()
            break
        elif choice == "1":
            print_all_products()
        elif choice == "2":
            print_all_suppliers()
        elif choice == "3":
            get_product_details_from_cli()
        elif choice == "4":
            get_supplier_details_from_cli()
        else:
            print("Invalid choice. Please try again.")
