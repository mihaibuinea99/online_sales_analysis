# product_manager.py
from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product: {product.name}")

    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Removed product: {name}")
                return True
        print(f"Product '{name}' not found.")
        return False

    def display_all_products(self):
        print("\n--- Available Products ---")
        if not self.products:
            print("No products available.")
        for product in self.products:
            product.display_info()
        print("-" * 26)

    def calculate_total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value