# online_sales_analysis
# Online Sales Analysis Project

## Descrierea proiectului
Acest proiect implementeaza un sistem simplu de gestionare a produselor, a stocurilor si a unui cos de cumparaturi pentru o platforma de vanzari online.

## Clase si functionalitati

### 1. Product (`product.py`)
Reprezinta un produs individual.
- **Atribute:** `name`, `price`, `quantity`.
- **Metode:**
  - `display_info()`: Afiseaza detalii despre produs.
  - `update_quantity(new_quantity)`: Actualizeaza stocul produsului.

### 2. ProductManager (`product_manager.py`)
Gestioneaza catalogul de produse disponibile.
- **Atribute:** `products` (lista de produse).
- **Metode:**
  - `add_product(product)`: Adauga un produs nou in catalog.
  - `remove_product(name)`: Elimina un produs din catalog dupa nume.
  - `display_all_products()`: Afiseaza toate produsele disponibile.
  - `calculate_total_inventory_value()`: Calculeaza valoarea totala a intregului inventar.

### 3. Cart (`cart.py`)
Gestioneaza cosul de cumparaturi al clientului.
- **Atribute:** `cart_items` (lista de produse selectate in cos).
- **Metode:**
  - `add_to_cart(product, quantity)`: Adauga produse in cos.
  - `calculate_cart_total()`: Calculeaza suma totala de plata.
  - `display_cart()`: Afiseaza continutul cosului si subtotalurile.

### 4. Main (`main.py`)
Scriptul principal care integreaza toate functionalitatile, creeaza instanta managerului de produse, adauga articole arbitrare, selecteaza produse aleatorii in cos si afiseaza rezultatele.