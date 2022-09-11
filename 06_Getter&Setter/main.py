import csv

class Item():
    # here we can declare class attributes
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: int, quantity = 0):
        assert price >= 0, f"Price {price} must be equal or greater than zero"
        assert quantity >= 0, f"Quantity {quantity} must be equal or greater than zero"

        # here we assign instance attributes
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    # getter
    @property
    def name(self):
        return self.__name

    # setter
    @name.setter
    def name(self, newname):
        assert len(newname) <= 10, f"New name: {newname} exceed 10 chars"
        self.__name = newname

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}(name: {self.name}, price: {self.price}, quantity: {self.quantity})"

    @staticmethod
    def is_integer(num):
        if isinstance(num, int):
            return True
        else:
            return False

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

# create a child class called Phone
class Phone(Item):
    def __init__(self, name: str, price: int, quantity = 0, broken_phones = 0):
        # call super method to initialize parameters in parent class
        super().__init__(name, price, quantity)

        # validate broken_num
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        self.broken_phones = broken_phones

phone1 = Phone("iphone", 1000, 3, 1)
# direct access to private attribute will raise error
# print(phone1.__name)
# AttributeError: 'Phone' object has no attribute '__name'

# use getter
print(phone1.name)
# use setter
phone1.name = "samsumg"
print(phone1.name)