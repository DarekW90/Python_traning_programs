# Kiedy używać metod class a kiedy używać metod static?

class Item:
    @staticmethod
    def is_integer():
        '''
        Powinno być wykorzystywane do czegoś co jest w związku z klasa,
        ale nie do czegoś co musi być unikatowe w danej instancji
        '''

    @classmethod
    def instance_from_something(cls):
        '''
        Powinno to również zrobić coś, co ma związek z klasą, 
        ale zwykle są one używane do manipulowania różnymi 
        strukturami danych w celu tworzenia instancji obiektów, 
        tak jak było to robione z CSV.
        '''


item1 = Item()
item1.is_integer(5)
item1.instance_from_something()