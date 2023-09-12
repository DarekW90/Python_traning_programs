from requests import get
from json import loads
from terminaltables import AsciiTable

# start menu
def userChoice():
    print()
    print('What kind of data do you want to see:')
    print('1. Data collected from all available stations')
    print('2. Data from selected stations')
    
    while True:
        userInput = input('Please select(1/2): ')
        if userInput in ['1','2']:
            return int(userInput)
        else:
            print('Invalid input. Please enter 1 or 2')
    
    
# request
def reciveData():
    CITIES = input('Input your city here: ')
    data = CITIES.split(',')
    cleanedData = [city.strip().replace(' ', '')
                   for city in data]  # Remove spaces
    cleanedData = ",".join(cleanedData)
    return cleanedData

# clear request
def getCities():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    # print(get(url))
    response = get(url)

    return response

# print all data def
def allData():
    response = getCities()

    rows = [
        ['Miasto:'.center(15), 'Godzina pomiaru:'.center(15), 'Temperatura:'.center(15),
            'Prędkość wiatru'.center(15), 'Opady'.center(15), 'Ciśnienie:'.center(15)]
    ]

    for row in loads(response.text):
        city = row['stacja']
        observation_time = row['godzina_pomiaru']
        temperature = row['temperatura']
        wind_speed = row['predkosc_wiatru']
        rain = row['suma_opadu']
        pressure = row['cisnienie']
        
        rows.append([(str(city).center(15)), 
                    (str(observation_time).center(15)), 
                    (str(temperature).center(15)), 
                    (str(wind_speed) + ' km/h').center(15), 
                    ((str(rain) + ' mm').center(15)), 
                    (str(pressure)).center(15) 
                    ])

    table = AsciiTable(rows)
    print(table.table)
    
    
# print only selected towns
def selectedData():
    CITIES = reciveData()
    response = getCities()

    rows = [
        ['Miasto:'.center(15), 'Godzina pomiaru:'.center(15), 'Temperatura:'.center(15),
            'Prędkość wiatru'.center(15), 'Opady'.center(15), 'Ciśnienie:'.center(15)]
    ]

    foundCities = set()

    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'].center(15),
                row['godzina_pomiaru'].center(15),
                row['temperatura'].center(15),
                (str(row['predkosc_wiatru']) + ' km/h').center(15),
                (str(row['suma_opadu']) + ' mm').center(15),
                row['cisnienie'].center(15)
            ])
            
            foundCities.add(row['stacja'])

    for city in CITIES.split(','):
        if city not in foundCities:
            rows.append([
                city.center(15),
                'Error'.center(15, '-'),
                'No'.center(15, '-'),
                'Data'.center(15, '-'),
                ''.center(15, '-'),
                ''.center(15, '-')
            ])

    table = AsciiTable(rows)
    print(table.table)



def main():
    user = userChoice()
    
    if user == 1:
        allData()
    elif user == 2:
        selectedData()
    


if __name__ == '__main__':
    print('Weather: ')
    main()
