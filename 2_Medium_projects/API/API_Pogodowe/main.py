from requests import get
# from json import load # odczyt z pliku lokalnego
from json import loads  # 'S' - string (loadString) odczyt ze stringu
from terminaltables import AsciiTable

CITIES = ['Gdańsk', 'Warszawa', 'Lublin', 'Wrocław']


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    print(get(url))
    response = get(url)
    rows = [
        ['Miasto:','Godzina pomiaru:','Temperatura:']
    ]
    # print(response.text) # text
    # print(loads(response.text)) # lista słowników

    # for row in loads(response.text):
    #    print(row)

    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])
    table = AsciiTable(rows)
    print(table.table)
    
    # 2xx - wszystko jest OK
    # 3xx - przekierowanie
    # 4xx - użytkownik coś zepsuł
    # 5xx - coś się stało po stronie serwera


if __name__ == '__main__':
    print('Pogodynka')
    main()
