class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def remove_from_cart(self, product_name):
        self.cart_items = [p for p in self.cart_items if p.name != product_name]

    def calculate_total(self):
        return sum(p.price for p in self.cart_items)

    def display_cart(self):
        for item in self.cart_items:
            print(item.display_info())