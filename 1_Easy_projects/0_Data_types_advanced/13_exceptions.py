# Wyjątki - exceptions - służą do obsługi błędów i sytuacji wyjątkowych

''' Przykład '''


def dzielenie(a, b):
    try:
        wynik = a / b
        return wynik
    except ZeroDivisionError as e:
        print(f'Błąd: {e} - próba dzielenia przez zero')

# Przykładowe wywołania funkcji dzielenie


print(dzielenie(10, 2))  # Wynik: 5
print(dzielenie(5, 0)) # Wynik: Błąd: division by zero - próba dzielenia przez zero
print(dzielenie(10, 3))
