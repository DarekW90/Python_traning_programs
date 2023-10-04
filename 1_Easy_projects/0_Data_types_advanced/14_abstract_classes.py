# Klasy abstrakcyjne - abstract classes - to taka klasa która nie może byćinstancjonowana, ale może zawierać metody które muszą być zaimplementowane w klasach dziedziczących.

from abc import ABC, abstractclassmethod


class Zwierze(ABC):
    @abstractclassmethod
    def dzwiek(self):
        pass


class Pies(Zwierze):
    def dzwiek(self):
        return 'Hau!'


class Kot(Zwierze):
    def dzwiek(self):
        return 'Meow!'


# W tym momencie próba utworzenia instancji klasy Zwierze spowoduje błąd
'''
Zwierze()

TypeError: Can't instantiate abstract class Zwierze with abstract method dzwiek
'''

# Ale można utworzyć instancje klas dziedziczących:

pies = Pies()
print(pies.dzwiek())  # Wypisze: Hau!

kot = Kot()
print(kot.dzwiek())  # Wypisze: Meow!
