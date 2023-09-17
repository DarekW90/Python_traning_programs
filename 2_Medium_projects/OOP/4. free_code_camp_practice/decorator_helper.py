# When to use class methods and when to use static methods ?

class Item:
    pass

    @staticmethod
    def is_integer():
        pass
        '''
        @staticmethod: 
        powinno robić coś co ma połączenie z klasa, 
        ale nie coś co musi być unikatowe dla instancji
        '''
        
    @classmethod
    def instantiate_from_something(cls):
        pass
    def instantiate_from_json_file(cls):
        pass
    def instantiate_from_ymal_file(cls):
        pass

        '''
        @classmethod:
        To powinno wykonywać coś co ma związek z klasą, 
        lecz przeważnie z tym co musi manipulować różnymi rodzajami struktur danych by inicjować obiekt, 
        tak jak było to wcześniej robione z plikiem CSV.
        '''
        
        
# aczkolwiek, mogą być wywoływane zpośród instancj

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()