import requests
from bs4 import BeautifulSoup
import re  # do usunięcia problemu z km/h połączonym na stałe z mph

while True:
    try:
        miasto = input("\nPodaj nazwę miasta: ").lower()
        url = ("https://www.google.pl/search?q=pogoda+" + miasto)

        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=header)

        soup = BeautifulSoup(response.content, "lxml")
        city = soup.find("span", class_="BBwThe")

        #Miasto
        print("\nPrognoza pogody dla miasta:", city.text)

        #opis ogólny
        general_description = soup.find("div", class_="wob_dcp")
        print("Opis ogólny:", general_description.text, "\n")

        #opis szczegółowy
        temperature_in_celsius = soup.find("span", class_="wob_t q8U8x")
        #print("Aktualna temperatura:", temperature_in_celsius.text, "℃")
        print("Aktualna temperatura:", temperature_in_celsius.text, "\u2103")


        rest_params = soup.find("div", class_="wtsRwe")
        for rest_param in rest_params:
            text = rest_param.text
            if "Wilgotność" in text:
                text = text.replace("Wilgotność:", "Wilgotność powietrza:")
            if "Wiatr" in text:
                text = text.replace("Wiatr:", "Prędkość wiatru:")
                text = re.sub(r'\d+\s*mph', '', text) #usunięcie informacji o predkości wiatru w milach/h
                text = re.sub(r'(\d+)\s+(km/h)', r'\1\2', text) #usunięcie spacji miedzy (cyfra)km/h
            print(text)

        answer = input("\nCzy chcesz powtórzyć program? (t/n): ")
        if answer.lower() == "n":
            break
    except Exception as e:
        print("Wystąpił błąd:", e)


