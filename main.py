from product import Product
from product_manager import ProductManager
from cart import Cart

# Initialize Product Manager
manager = ProductManager()

# Add some products
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Phone", 800, 10))
manager.add_product(Product("Headphones", 150, 20))

# Display all products
manager.display_products()
print(f"Total Inventory Value: {manager.total_inventory_value()}")

# Remove a product
manager.remove_product("Phone")
print("After removal:")
manager.display_products()

# Initialize Cart
cart = Cart()
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])

# Display cart items
cart.display_cart()
print(f"Total Cart Value: {cart.calculate_total()}")

# Remove an item from the cart
cart.remove_from_cart("Laptop")
print("After removing from cart:")
cart.display_cart()