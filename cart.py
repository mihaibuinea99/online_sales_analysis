# cart.py

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity=1):
        # Putem adauga produsul impreuna cu cantitatea dorita
        item = {"product": product, "quantity": quantity}
        self.cart_items.append(item)
        print(f"Added {quantity} x {product.name} to the cart.")

    def calculate_cart_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return total

    def display_cart(self):
        print("\n--- Shopping Cart Contents ---")
        if not self.cart_items:
            print("The cart is empty.")
        for item in self.cart_items:
            prod = item["product"]
            qty = item["quantity"]
            subtotal = prod.price * qty
            print(f"Product: {prod.name} | Price: ${prod.price:.2f} | Quantity: {qty} | Subtotal: ${subtotal:.2f}")
        print(f"Total Cart Value: ${self.calculate_cart_total():.2f}")
        print("-" * 30)