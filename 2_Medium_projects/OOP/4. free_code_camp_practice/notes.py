####################################################

item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1))  # str
print(type(item1_price))  # int
print(type(item1_price_total))  # int
print(type(item1_price_total))  # int
print()

####################################################


class Item:
    pass


# item1 jest instancją Item()
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

print(type(item1))  # item
print(type(item1.name))  # str
print(type(item1.price))  # int
print(type(item1.quantity))  # int
print()

####################################################

random_str = 'aaa'
print(random_str.upper())
print()

####################################################


class Item:
    def __init__(self):
        print('I AM CREATED!')


item1 = Item()
item2 = Item()
item3 = Item()
print()

####################################################


class Item:
    def __init__(self, name):
        print(f'An instance created: {name}')


item1 = Item('Phone')
item2 = Item('Laptop')
print()

####################################################


class Item:
    def __init__(self, name):
        self.name = name


item1 = Item('Phone')
item2 = Item('Laptop')
print(item1.name)
print(item2.name)
print()

####################################################


class Item:
    def __init__(self, name, price, quantity):
        # print(f'An instance created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity


item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

print(item1.name)
print(item2.name)
print(item1.quantity)
print(item2.quantity)
print(item1.price)
print(item2.price)
print()

####################################################


class Item:
    def __init__(self, name, price, quantity=0):
        # print(f'An instance created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print()

####################################################

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recived arguments
        assert price >= 0 ,f'Price {price} is not greater than 0!'
        assert quantity >= 0,f'Quantity {quantity} is not greater than 0!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


#item1 = Item('Phone', 100, -5)
#item2 = Item('Laptop', 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print()

####################################################

