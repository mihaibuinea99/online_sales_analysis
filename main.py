# main.py
from product import Product
from product_manager import ProductManager

def main():
    # Crearea instantei ProductManager
    manager = ProductManager()

    # Denumiri si cantitati schimbate fata de ramura add-cart-functionality
    p1 = Product("Gaming Laptop", 1400.00, 3)
    p2 = Product("Wireless Mouse", 35.50, 25)
    p3 = Product("Mechanical Keyboard", 90.00, 15)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Liniile legate de afisarea inventarului au fost sterse conform cerintei.

if __name__ == "__main__":
    main()