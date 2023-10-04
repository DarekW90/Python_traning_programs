# Dekoratory - decorators - pozwalają na zmianę lub rozszerzanie funkcjonalności istniejących funkcji.

''' Przykład '''

print()


def dekorator(funkcja):
    def opakowanie(*args, **kwargs):
        print('Wykonywanie dodatkowych czynności przed wywowłaniem funkcji')
        wynik = funkcja(*args, **kwargs)
        print('Wykonanie dodatkowych czynności po wywołaniu funkcji')
        return wynik
    return opakowanie


@dekorator
def przykładowa_funkcja():
    print('To jest przykładowa funkacja')

# teraz wywołanie ' przykładowa_funkcja() ' spowoduje dodatkowe czynności zdefiniowane w dekoratorze
przykładowa_funkcja()

print()
