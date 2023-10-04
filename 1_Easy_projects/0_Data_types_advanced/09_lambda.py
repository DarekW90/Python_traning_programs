# Wyrażenia lambda - lambda expressions - pozwalają na tworzenie małych funkcji anonimowych
# Funkcja anonimowa odnosi się do funkcji, która nie ma nazwy, czyli nie jest związana z konkretną identyfikacją w programie.

# W Pythonie wyrażenia lambda są to małe funckje, które nie wymagają definiowania nazwy za pomocą słowa kluczowego 
# "def". Zamiast tegom są one zdefiniowane za pomocą słowa kluczowego "lambda" i są często używane do wykonywania prostych operacji
# lub obliczeń w miejscu, gdzie funkcja jest potrzebna tylko w jednym konkretnym kontekscie.

# W skrócie:
#     Funkcje anonimowe (lub lambda) są używane tam, gdzie potrzebujemy krótkiej i jednorazowej funkcji bez konieczności nadawania jej stałej nazwy w programie.

''' Przykład '''

dodaj = lambda x,y : x+y

wynik = dodaj(3,4)

print(f'Wynik 3+4 otrzymany przy pomocy wyrażenia lambda: {wynik}')