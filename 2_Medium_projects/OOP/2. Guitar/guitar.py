class Guitar:
    def __init__(self, n_strings=6): # default 6 strings
        self.n_strings = n_strings
        self.play()  # dla pkt nr # 3
        self.__cost = 50

    def play(self):
        # play() - funkcja
        # object.play() - objekt
        print('pam pam pam pam pam pam pam')

# 1
# my_guitar = Guitar()
# print(my_guitar.n_strings)

# 2
# my_guitar = Guitar()
# print(my_guitar.n_strings)

# my_guitar.play()

# 3
# my_guitar = Guitar()

# 4 Dziedziczenie - ElectricGuitar przejmuje informacje od Guitar

# class ElectricGuitar(Guitar):
#     def playLauder(self):
#         print('pam pam pam pam pam pam pam'.upper())


# my_guitar = ElectricGuitar()
# print(my_guitar.n_strings)
# my_guitar.playLauder()

# 5 edycja dziedziczenia
class ElectricGuitar(Guitar):
    def __init__(self):
        # super - zezwala na edycje danych otrzymanych od rodzica przez dziedziczenie
        super().__init__(n_strings = 8)
        self.color = ('#000000', '#FFFFFF')
        # __.cost ustawia status private dla cost
        #self.__cost = 50

    def playLauder(self):
        print('pam pam pam pam pam pam pam'.upper())

    def __secret(self):
        print('this guitar actualy cost me $', self._Guitar__cost, 'only!')

class BassGuitar(Guitar):
    pass


my_guitar = ElectricGuitar()
print(my_guitar.n_strings)
my_guitar.playLauder()
print('child class: ', my_guitar.n_strings)
print('parent class: ', Guitar().n_strings)
# print()
# print(my_guitar.__cost)
print()
#print(my_guitar._ElectricGuitar__cost)
print()
my_guitar._ElectricGuitar__secret()
print()
print('my bass guitar has ', BassGuitar(4).n_strings, 'strings')
print()
print('my electric guitar has ', my_guitar.n_strings, 'strings')


