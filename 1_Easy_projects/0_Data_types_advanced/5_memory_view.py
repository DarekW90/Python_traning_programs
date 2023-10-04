# Buffory pamięci - memoryview - pozwalają na widok i manipulację danymi w buforach pamięci bez koniecznośći ich kopiowania.
# Przykład:
#     bufor = memoryview(b'hello')

bufor = memoryview(b'hello')
print(f'Wywołany buffor w pamięci: {bufor}')