# Funkcje - functions - W Pythonie funkcje są obiektami pierwszej klasym co oznacza,
# że można je przypisywać do zmiennych, przekazywać jako argumenty i zwracać jako wartości.

''' Przykład '''


def dodaj(a, b):
    return a+b


przykładowa_funkcja = dodaj
wynik = przykładowa_funkcja(3, 4)

print(f'Wynik dodawania 3+4={wynik}')
