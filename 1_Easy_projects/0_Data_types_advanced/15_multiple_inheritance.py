# dziedziczenie wielokrotne - multiple inheritance - pozwala na dziedziczenie właściwości z wielu klas nadrzędnych

class A:
    def metoda_a(self):
        print('Metoda z klasy A')


class B:
    def metoda_b(self):
        print('Metoda z klasy B')


class C(A, B):
    pass


obiekt_c = C()
obiekt_c.metoda_a()  # wypisze: "Metoda z klasy A"
obiekt_c.metoda_b()  # wypisze: "Metoda z klasy B"
