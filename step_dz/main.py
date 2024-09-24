class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.products:
            total_cost += product.price * product.quantity
        return total_cost

    def __str__(self):
        cart_contents = "Cart Contents:\n"
        for product in self.products:
            cart_contents += f"- {product}\n"
        cart_contents += f"Total Cost: {self.calculate_total_cost()}"
        return cart_contents
product_1 = Product("Apple", 10, 2)
product_2 = Product("Banana", 5, 3)

cart = Cart()
cart.add_product(product_1)
cart.add_product(product_2)
print(cart)
cart.remove_product(product_2)
print(cart)