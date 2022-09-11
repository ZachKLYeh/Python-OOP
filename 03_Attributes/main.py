class Item():
    # here we can declare class attributes
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: int, quantity = 0):
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # here we assign instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # we can do some operation on class attributes
        # Note: class attrubutes can only access py template, not instance
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    # Item.all = [<__main__.Item object at 0x7ff83a16f5f8>]
    # we can modify the way that class attributes are displayed by __repr__
    def __repr__(self):
        return f"Item(name: {self.name}, price: {self.price}, quantity: {self.quantity})"

item1 = Item("candy", 3, 10)
print(Item.all)
item2 = Item("coockie", 20, 10)
print(Item.all)