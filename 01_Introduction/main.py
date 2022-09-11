# create a example class
class Item():
    # create a method in a class
    def calculate_total_price(self, quantity, price):
        return quantity * price

# create a instance of the class
item1 = Item()

# assign attributes (Note: these attributes are not initialized)
item1.quantity = 3
item1.price = 10
item1.name = "candy"

# calling method of the class
print(item1.calculate_total_price(item1.quantity, item1.price))

# create another instance
item2 = Item()

# assign attribute
item2.quantity = 10
item2.price = 20
item2.name = "coockie"

print(item2.calculate_total_price(item2.quantity, item2.price))