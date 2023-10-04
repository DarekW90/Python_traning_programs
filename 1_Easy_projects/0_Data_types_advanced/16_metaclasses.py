# Metaklasy - metaclasses - zaawansowany koncept w Pythonie, który umożliwia kontrolowanie sposobu, w jaki są tworzone klasy.

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'Tworzenie nowej klasy: {name}')
        cls_instance = super().__new__(cls, name, bases, dct)
        return cls_instance


class MojaKlasa(metaclass=Meta):
    def moja_metoda(self):
        print("To jest moja metoda")

# Po utworzeniu obiektu klasy MOjaKlasa zostanie wypisany komunikat z metaklasy Meta


moj_obiekt = MojaKlasa()
moj_obiekt.moja_metoda()
