from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os


class D2Login:
    def __init__(self):
        self.driver = self.init_driver()
        
    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        return webdriver.Chrome(options=options)
        
    def login(self, url, login_file):
        self.driver.get(url)
        self.driver.maximize_window()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'login.txt')

        with open(file_path, 'r') as file:
            lines = file.readlines()
            
        if len(lines) >= 2:
            login = lines[0].strip()
            password = lines[1].strip()
        else:
            print('plik nie zawiera wystarczającej liczby danych.')

        time.sleep(1)

        login_box = self.driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[1]/input')
        login_box.send_keys(login)
        password_box = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/input')
        password_box.send_keys(password, Keys.ENTER)
        time.sleep(2)
        #przejdź na trade page
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/nav/div[2]/a[2]').click()
        time.sleep(2)
        # klik w create
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[2]/div/span').click()
        time.sleep(2)
        # click w wybierz okienko
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
        time.sleep(2)
        # click w strone (tu 9)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select/option[11]').click()
        time.sleep(2)
        # zatwierdzenie wyboru
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
        time.sleep(2)
        # wyszukaj
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/button[1]').click()
        # klik add
        
        page_counter = 0
        while page_counter <= 5:
            counter = 1
            
            while counter <= 30:
                time.sleep(0.5)
                print(f'loop number: {counter}')
                try:
                    element = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[1]/div[2]/div[1]/div[1]')
                    element.click()
                    price_box = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[2]/div/div[1]/input')
                    price_box.send_keys('pul / 0.03 HR / 2 wss / 14 pgems / 9 reroll runes')
                    price_box.click()
                    
                    set_price = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[2]/div/div[4]')
                    set_price.click()
                    counter += 1
                    
                    #element = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div/div[2]/div[1]/div[1]').click()
                    
                except NoSuchElementException:
                    print(f'Element o indeksie {counter} nie został znaleziony')
                    counter += 1
            try:   
                page = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/button[{page_counter}]')
                page.click()
                page_counter += 1
            except NoSuchElementException:
                print(f'Nie znaleziono guzika page: {page_counter}')
                page_counter += 1
        
        
        time.sleep(10)

    
    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    login_manager = D2Login()
    login_manager.login('https://www.projectdiablo2.com/login','login.txt')
    login_manager.close()