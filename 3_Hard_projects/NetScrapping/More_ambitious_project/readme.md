## This is scraper for collecting data of PS4 game price from ultima.pl

<h1>Step 1: Importing Libraries</h1>

> import mechanicalsoup<br>
> import os<br>
> import time<br>
> import pandas as pd

In this step, we import the necessary libraries and modules:<br><br>
<b>mechanicalsoup:</b> - Enables browsing and manipulation of web pages.<br>
<b>os:</b> - Provides functions for file system operations.<br>
<b>time:</b> - Allows working with time.<br>
<b>pandas:</b> - A library for data analysis, especially for data manipulation in tabular form (DataFrame).<br>

<h1>Step 2: Creating the GameScraper Class</h1>

> class GameScraper:

Here we begin to define the GameScraper class, which will contain all the functionalities related to web scraping.

<h1>Step 3: The __init__ Method</h1>

> def __init__(self):<br>
>    self.data = {'Game': [], 'Status': [], 'Price': []}<br>
>    self.page = 1<br>
>    self.start_time = time.time()<br>
>    self.browser = mechanicalsoup.StatefulBrowser()<br>

The <b>__init__</b> method is a special method that is called during the initialization of an object of this class.<br>
In this case, upon object initialization, the following actions are performed:<br>
- Creation of an empty dictionary 'data' to store game information.<br>
- Setting 'page' to 1 - indicating that we start from the first page.<br>
- Recording the current time as 'start_time'.<br>
- Creating a browser object using the MechanicalSoup library.<br>

<h1>Step 4: The scrape_page Method</h1>

> def scrape_page(self):<br>
>    url = f```https://www.ultima.pl/ct/playstation-4/gry/?page\={self.page}```<br>
>    self.browser.open(url)<br>
>
>    products = self.browser.page.find_all('div', attrs={'class': 'product-title'})<br>
>    products_status = self.browser.page.find_all('div', attrs={'class': 'product-status-text'})<br>
>    prices = self.browser.page.find_all('div', attrs={'class': 'product-price'})<br>
>
>    for product in products[3:]:<br>
>        product_name = product.text.strip()<br>
>        self.data['Game'].append(product_name)<br>
>
>    for status in products_status:<br>
>        status_text = status.text.strip()<br>
>        self.data['Status'].append(status_text)<br>
>
>    for price in prices[10:]:<br>
>        price_text = price.text.strip()<br>
>        if len(price_text) > 0:<br>
>            price_edited = price_text[:-4] + '.' + price_text[-4:]<br>
>            self.data['Price'].append(price_edited)<br>
>        else:<br>
>            self.data['Price'].append('NoData')<br>
>
>    self.last_index += 1<br>
>    self.page += 1<br>

The <b>scrape_page</b> method is responsible for scraping data from a specific page.<br>
It creates the appropriate URL for that page and opens it using the browser.<br>
It then finds and saves information about games, their statuses, and prices to the 'data' dictionary.<br>

<h1>Step 5: The run Method</h1>

> def run(self):<br>
>    while self.page < 2:  # You can change this condition to fetch more pages<br>
>        print(f'Checking page number: {self.page}')<br>
>        self.scrape_page()<br>
>
>    self.stop_time = time.time()<br>
>    self.run_time = self.stop_time - self.start_time<br>
>    self.formatted_run = time.strftime("%H:%M:%S", time.gmtime(self.run_time))<br>
>
>    df = pd.DataFrame(self.data)<br>
>
>    current_file_path = os.path.abspath(__file__)<br>
>    current_directory = os.path.dirname(current_file_path)<br>
>    data_directory = os.path.join(current_directory, 'data')<br>
>    os.makedirs(data_directory, exist_ok=True)<br>
>
>    csv_path = os.path.join(data_directory, 'data.csv')<br>
>
>    df.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')<br>
>
>    print(f'Program run time: {self.formatted_run}')<br>

The <b>run</b> method is the main method that controls the scraping process.<br>
In this case, the program will scrape pages until 'self.page' reaches 2.<br>
You can change this condition to fetch more pages.<br>
After the scraping is complete, the execution time is calculated, and a DataFrame 'df' is created with the data.<br>
Then a directory named "data" is created, and a CSV file with the data is saved.<br>

<h1>Step 6: Running the Program</h1>

> if __name__ == '__main__':<br>
>    scraper = GameScraper()<br>
>    scraper.run()<br>

In this step, we check if the script is run as the main program, not imported as a module.<br>
If so, we create an object of the GameScraper class named 'scraper' and execute the 'run' method.<br>


***

## To scraper do zbierania danych o cenach gier PS4 ze strony ultima.pl

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
>        url = f```https://www.ultima.pl/ct/playstation-4/gry/?page\={self.page}```<br>
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

>    def run(self):<br>
>        while self.page < 2:  # Możesz zmienić ten warunek, aby pobrać więcej stron<br>
>            print(f'Sprawdzam strone nr: {self.page}')<br>
>            self.scrape_page()<br>
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

run to główna metoda, która steruje procesem scrapowania.<br>
W tym przypadku, program będzie scrapował strony dopóki self.page nie osiągnie 2.<br>
Możesz zmienić ten warunek, aby pobrać więcej stron.<br>
Po zakończeniu scrapowania, zostanie obliczony czas wykonania i utworzony zostanie DataFrame df z danymi.<br>
Następnie zostanie utworzony katalog "data" i zapisany zostanie plik CSV z danymi.<br>

<h1>Krok 6: Uruchomienie Programu</h1>

>   if __name__ == '__main__':<br>
>    scraper = UltimaScraper()<br>
>    scraper.run()<br>

W tym kroku, sprawdzamy czy skrypt został uruchomiony jako główny program, a nie jako moduł importowany.<br>
Jeśli tak, tworzymy obiekt klasy GameScraper o nazwie scraper i uruchamiamy metodę run.