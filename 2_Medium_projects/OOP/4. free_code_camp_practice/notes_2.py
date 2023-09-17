# dekoratory

import csv
import os


class Item:
    # class atribute
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the recived arguments
        assert price >= 0, f'Price {price} is not greater than 0!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than 0!'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    ''' DEKORATOR class method '''
    
    @classmethod
    def instantiate_from_csv(cls):
        current_file_path = os.path.abspath(__file__)  # Pobierz pełną ścieżkę do aktualnego pliku
        current_directory = os.path.dirname(current_file_path)
        file_path = os.path.join(current_directory, 'items.csv')  # Połączenie z nazwą pliku
        
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        # for item in items:
        #     print(item)
            
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # __repr__ -> represent your object
    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'


Item.instantiate_from_csv()
print(Item.all)
