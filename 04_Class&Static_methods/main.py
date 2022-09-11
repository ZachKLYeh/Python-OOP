import csv

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

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"Item(name: {self.name}, price: {self.price}, quantity: {self.quantity})"

    @staticmethod
    def is_integer(num):
        """
        static method mas no relation with an instance,
        is more like a function, it cannot access class attributes
        except that it can only be access via class or instance
        """
        if isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def instantiate_from_csv(cls):
        """
        different from static method
        class method require "cls" argment
        and have access to class attributes
        which is often used to load data
        BTW, class and static methods can all be called by class
        """
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(3.2))