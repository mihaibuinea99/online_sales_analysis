# main.py
import random
from product import Product
from product_manager import ProductManager
from cart import Cart

def main():
    # Crearea instantei ProductManager
    manager = ProductManager()

    # Denumiri si cantitati schimbate fata de ramura add-cart-functionality
    p1 = Product("Gaming Laptop", 1400.00, 3)
    p2 = Product("Wireless Mouse", 35.50, 25)
    p3 = Product("Mechanical Keyboard", 90.00, 15)
    p4 = Product("HD Monitor", 250.00, 10)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)

    # Afisarea tuturor produselor
    manager.display_all_products()

    # Afisarea valorii totale a inventarului
    total_value = manager.calculate_total_inventory_value()
    print(f"Total inventory value: ${total_value:.2f}")

    # --- Etapa 6: Lucrul cu clasa Cart ---
    print("\n--- Cart Operations ---")
    cart = Cart()

    # Selectarea a 3 produse aleatorii din lista disponibila
    if len(manager.products) >= 3:
        random_products = random.sample(manager.products, 3)
        for product in random_products:
            # Adaugam o cantitate aleatorie intre 1 si 3 pentru fiecare produs in cos
            qty = random.randint(1, 3)
            cart.add_to_cart(product, qty)

    # Afisarea continutului cosului si a valorii totale de plata
    cart.display_cart()

if __name__ == "__main__":
    main()