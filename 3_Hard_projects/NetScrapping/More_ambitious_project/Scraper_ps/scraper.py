import mechanicalsoup
import os
import time
import pandas as pd

class GameScraper:
    def __init__(self):
        self.data = {'Game': [], 'Status': [], 'Price': []}
        self.page = 1
        self.start_time = time.time()
        self.browser = mechanicalsoup.StatefulBrowser()

    def scrape_page(self):
        url = f'https://www.ultima.pl/ct/playstation-4/gry/?page={self.page}'
        self.browser.open(url)

        products = self.browser.page.find_all('div', attrs={'class': 'product-title'})
        products_status = self.browser.page.find_all('div', attrs={'class': 'product-status-text'})
        prices = self.browser.page.find_all('div', attrs={'class': 'product-price'})

        for product in products[3:]:
            product_name = product.text.strip()
            if 'PS4' in product_name or 'PS5' in product_name:
                product_name = product_name.replace('PS4', '').replace('PS5', '')
            self.data['Game'].append(product_name)

        for status in products_status:
            status_text = status.text.strip()
            self.data['Status'].append(status_text)

        for price in prices[10:]:
            price_text = price.text.strip()
            if len(price_text) > 0:
                price_edited = price_text[:-4] + '.' + price_text[-4:]
                self.data['Price'].append(price_edited)
            else:
                self.data['Price'].append('NoData')

        self.page += 1

    def run(self):
        while self.page < 10:  # Change this condition if needed
            print(f'Page number: {self.page}')
            self.scrape_page()

        self.stop_time = time.time()
        self.run_time = self.stop_time - self.start_time
        self.formatted_run = time.strftime("%H:%M:%S", time.gmtime(self.run_time))

        df = pd.DataFrame(self.data)

        current_file_path = os.path.abspath(__file__)
        current_directory = os.path.dirname(current_file_path)
        data_directory = os.path.join(current_directory, 'data')
        os.makedirs(data_directory, exist_ok=True)

        csv_path = os.path.join(data_directory, 'playstation_data.csv')

        df.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')

        print(f'Program run time: {self.formatted_run}')


if __name__ == '__main__':
    scraper = GameScraper()
    scraper.run()
