# Klasy - classes - Pozwalają na tworzenie obiektów, które mogą mieć własne atrybuty - zmienne - i metody.

''' Przykład '''

class Zwierze:
    def __init__(self,gatunek,wiek):
        self.gatunek = gatunek
        self.wiek = wiek
        
    def opis(self):
        return f'To jest {self.gatunek}, ma {self.wiek} lat'
    
    def ustaw_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek
        
# tworzenie obiektu klasy Zwierze
moje_zwierze = Zwierze('Kot', 5)

# Wywołanie metody i odczytanie atrybutu
print(f'1. {moje_zwierze.opis()}')

# Zmiana wieku za pomocą metody
moje_zwierze.ustaw_wiek(6)

# Ponowne wywołanie opisu
print(f'2. {moje_zwierze.opis()}')