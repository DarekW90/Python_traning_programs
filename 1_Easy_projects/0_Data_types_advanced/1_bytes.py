# Bajty - bytes - reprezentują sekwencje bajtów.
# Są niemodyfikowalne, podobnie do krotek.
# Przykład:
#    bajty = b'hello'

słowo = 'hello'
bajty = b'hello'
print(f'Bajt pierwszej litery słowa {słowo}: {bajty[0]}')
print(f'Bajt drugiej litery słowa {słowo}: {bajty[1]}')
print(f'Bajt trzeciej litery słowa {słowo}: {bajty[2]}')
print(f'Bajt czwartej litery słowa {słowo}: {bajty[3]}')
print(f'Bajt piątej litery słowa  {słowo}: {bajty[4]}')

print('*'*45)
poskładane = bytes([104, 101, 108, 108, 111])
print(f'Słowo złożone z bitów: {poskładane}')
