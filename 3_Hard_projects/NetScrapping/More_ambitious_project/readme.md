## This is scraper for collecting data of PS4 game price from ultima.pl

<h1>Krok 1: Importowanie Bibliotek</h1>

>    import mechanicalsoup<br>
>    import os<br>
>    import time<br>
>    import pandas as pd

W tym kroku importujemy niezbędne biblioteki i moduły:<br><br>
<b>mechanicalsoup:</b> - Umożliwia przeszukiwanie i manipulację stronami internetowymi.<br>
<b>os:</b> - Dostarcza funkcje do operacji na systemie plików.<br>
<b>time:</b> - Umożliwia pracę z czasem.<br>
<b>pandas:</b> - Biblioteka do analizy danych, szczególnie do manipulacji danymi w postaci tabeli (DataFrame).<br>

<h1>Krok 2: Tworzenie Klasy GameScraper</h1>

>    class GameScraper:

Tutaj zaczynamy definiować klasę GameScraper, która będzie zawierała wszystkie funkcjonalności związane z scrapowaniem strony.

<h1>Krok 3: Metoda __init__</h1>

>    def __init__(self):<br>
>        self.data = {'Game': [], 'Status': [], 'Price': []}<br>
>        self.page = 1<br>
>        self.start_time = time.time()<br>
>        self.browser = mechanicalsoup.StatefulBrowser()<br>

<b>__init__ </b>to specjalna metoda, która jest wywoływana podczas inicjalizacji obiektu tej klasy.<br>
W tym przypadku, przy inicjalizacji obiektu, zostaną wykonane następujące czynności:<br>
Stworzenie pustego słownika data, który będzie przechowywał informacje o grach.<br>
Ustawienie page na 1 - oznacza to, że zaczynamy od pierwszej strony.<br>
Zapisanie bieżącego czasu jako start_time.<br>
Stworzenie obiektu przeglądarki (browser) z biblioteki MechanicalSoup.<br>


<h1>Krok 4: Metoda scrape_page</h1>

>    def scrape_page(self):
>        url = f`https://www.ultima.pl/ct/playstation-4/gry/?page={self.page}`
>        self.browser.open(url)
>
>        products = self.browser.page.find_all('div', attrs={'class': 'product-title'})
>        products_status = self.browser.page.find_all('div', attrs={'class': 'product-status-text'})
>        prices = self.browser.page.find_all('div', attrs={'class': 'product-price'})
>
>        for product in products[3:]:
>            product_name = product.text.strip()
>            self.data['Game'].append(product_name)
>
>        for status in products_status:
>            status_text = status.text.strip()
>            self.data['Status'].append(status_text)
>
>        for price in prices[10:]:
>            price_text = price.text.strip()
>            if len(price_text) > 0:
>                price_edited = price_text[:-4] + '.' + price_text[-4:]
>                self.data['Price'].append(price_edited)
>            else:
>                self.data['Price'].append('NoData')
>
>        self.last_index += 1
>        self.page += 1

<b>scrape_page</b> to metoda, która zajmuje się scrapowaniem danych z konkretnej strony.
Tworzony jest odpowiedni URL dla danej strony.
Przeglądarka otwiera ten URL.
Następnie znajduje i zapisuje informacje o grach, ich statusach oraz cenach do słownika data.


<h1>Krok 5: Metoda run</h1>

>    def run(self):
>        while self.page < 2:  # Możesz zmienić ten warunek, aby pobrać więcej stron
>            print(f'Sprawdzam strone nr: {self.page}')
>            self.scrape_page()
>
>        self.stop_time = time.time()
>        self.run_time = self.stop_time - self.start_time
>        self.formatted_run = time.strftime("%H:%M:%S", time.gmtime(self.run_time))
>
>        df = pd.DataFrame(self.data)
>
>        current_file_path = os.path.abspath(__file__)
>        current_directory = os.path.dirname(current_file_path)
>        data_directory = os.path.join(current_directory, 'data')
>        os.makedirs(data_directory, exist_ok=True)
>
>        csv_path = os.path.join(data_directory, 'dane.csv')
>
>        df.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')
>
>        print(f'Program run time: {self.formatted_run}')

run to główna metoda, która steruje procesem scrapowania.
W tym przypadku, program będzie scrapował strony dopóki self.page nie osiągnie 2. Możesz zmienić ten warunek, aby pobrać więcej stron.
Po zakończeniu scrapowania, zostanie obliczony czas wykonania i utworzony zostanie DataFrame df z danymi.
Następnie zostanie utworzony katalog "data" i zapisany zostanie plik CSV z danymi.

<h1>Krok 6: Uruchomienie Programu</h1>

>   if __name__ == '__main__':<br>
>    scraper = UltimaScraper()<br>
>    scraper.run()<br>

W tym kroku, sprawdzamy czy skrypt został uruchomiony jako główny program, a nie jako moduł importowany.
Jeśli tak, tworzymy obiekt klasy GameScraper o nazwie scraper i uruchamiamy metodę run.