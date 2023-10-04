# Generatory - generators - pozwalają na tworzenie sekwencji danych w sposób "leniwy" - czyli generowanie wartości na żądanie

# 'yield' jest słowem kluczowym w Pythonie używanym w kontekscie tworzenia generatorów.

''' Przykład '''


def generator_liczb_naturalnych(n):
    i = 0
    while i < n:
        yield i
        i += 1

# użycie generatora


for liczba in generator_liczb_naturalnych(10):
    print(liczba)
