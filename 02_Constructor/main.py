class Item():
    def __init__(self, name: str, price: int, quantity = 0):
        # We can add some restrictions of the value of parameters
        # assert (statement), (error message)
        # if the statement is not true, then show the defined error message
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # assign attributes with parameters
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# init a item
# item1 = Item("candy", 3, -1)
# AssertionError: Quantity -1 must be equal or greater than zero

item1 = Item("candy", 3, 10)
item2 = Item("coockie", 10 ,20)

print(item1.calculate_total_price())
print(item2.calculate_total_price())