# Wzorce - patterns - (python 3.10+) pozwalają na przeszukiwanie tekstów w bardziej zaawansowany sposób niż wyrażenia regularne.
# Przykład:
#     import re

#     wzorzec = re.compile(r'(\d+)')


import re

wzorzec = re.compile(r'\ba[a-z]*')

tekst = "ala ma kota, a kot ma ale."
wyniki = wzorzec.findall(tekst)

print(wyniki)  # Output: ['Ala', 'a', 'ale']
