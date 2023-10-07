from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os


class D2Login:
    def __init__(self, wss):
        self.driver = self.init_driver()
        self.rune_calculator(wss)
        
    def rune_calculator(self, wss):
        self.wss = wss
        self.runes = {
            'lum' : {'hr_rate' : 0.01},
            'ko' : {'hr_rate' : 0.01},
            'fal' : {'hr_rate' : 0.02},
            'lem' : {'hr_rate' : 0.02},
            'pul' : {'hr_rate' : 0.03},
            'um' : {'hr_rate' : 0.05},
            'mal' : {'hr_rate' : 0.1},
            'ist' : {'hr_rate' : 0.15},
            'gul' : {'hr_rate' : 0.25},
            'vex' : {'hr_rate' : 0.5},
            'ohm' : {'hr_rate' : 0.75},
            'lo' : {'hr_rate' : 1},
            'sur' : {'hr_rate' : 1.3},
            'ber' : {'hr_rate' : 2.6},
            'jah' : {'hr_rate' : 1.25},
            'cham' : {'hr_rate' : 1},
            'zod' : {'hr_rate' : 1.5}
        }
        
        
    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        return webdriver.Chrome(options=options)
        
    def start_select(self):
        print('!!!!!!!!!!!!!!!!!!!!')
        print('What would you like to do?')
        print('1. Add new trades')
        print('2. Delete old trades')
        
        while True:
            start_select = input('Please input a number: ')
            
            if start_select in ['1','2']:
                return int(start_select)
            else:
                print('Wrong input')
                
    def continue_or_close(self):
        print('No more value to show')    
        print('Continue or Close...?')
        
        while True:
            continue_or_close = input('')
            if continue_or_close in ['continue', 'close']:
                if continue_or_close == 'continue':
                    return True
                else:
                    return False
        
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
            print('Not enough data in login file.')

        time.sleep(1)

        login_box = self.driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[1]/input')
        login_box.send_keys(login)
        password_box = self.driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[2]/input')
        password_box.send_keys(password, Keys.ENTER)
        time.sleep(2)
        
            
        # go to trade page
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/nav/div[2]/a[2]').click()
        time.sleep(2)
        
        start_select = self.start_select()
        
        if start_select == 1:
            # click create
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[2]/div/span').click()
            time.sleep(2)
        
            # click select page
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
            # click w stash
            print('Which one stash should be checked?')
            print('1 for None')
            print('2 for Main')
            print('3 for Stash 1')
            print('4 for Stash 2')
            print('5 for Stash 3')
            print('6 for Stash 4')
            print('7 for Stash 5')
            print('8 for Stash 6')
            print('9 for Stash 7')
            print('10 for Stash 8')
            print('11 for Stash 9')
            print()
            stash = input('Please select: ')
            self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select/option[{stash}]').click()
            #time.sleep(2)
            # zatwierdzenie wyboru
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
            #time.sleep(2)
            # wyszukaj
            self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/button[1]').click()
            
            # klik add
            while True:
                counter = 1
                
                while counter <= 30:
                    time.sleep(0.1)
                    print(f'loop number: {counter}')
                    print()
                    try:
                        what_item = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[1]/div')
                        print(what_item.text)
                        print()
                        
                        set_price = None
                        
                        try:
                            give_price = input('Give price of item: ')
                            print()
                            rune_info = self.runes.get(give_price)
                            if rune_info is not None:
                                # rune_info = self.runes[give_price]
                                hr_rate = rune_info['hr_rate']
                                wss_price = round(hr_rate * self.wss)
                                pgem_price = wss_price * 7
                                reroll_price = round(pgem_price * (2/3))
                            
                                set_price = (f'{give_price} / {hr_rate} HR / {(wss_price)} wss / {pgem_price} pgems / {reroll_price} reroll runes')
                            else:
                                print('Rune not found in dictionary')
                                
                        except (KeyError, ValueError):
                            print('Wrong input')
                        
                        if set_price is not None:
                            # open set price window
                            add_button = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[1]/div[2]/div[1]/div[1]')
                            add_button.click()
                            list_info = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div/div[2]/div[1]/div[2]')
                            print(f'############### {list_info.text} ###############')
                            # put price into set price window
                            price_box = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[2]/div/div[1]/input')
                            price_box.send_keys(set_price)
                            # close info box 
                            price_box.click()
                            # set price and accept
                            set_price = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div[2]/div/div[4]')
                            set_price.click()
                            submit_info = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[1]/div/div[{counter}]/div[2]/div/div[1]/div[1]')
                            print(f'@@@@@@@@@@@@@@@ {submit_info.text} @@@@@@@@@@@@@@@')
                            counter += 1
                        else: 
                            pass
                        
                    except NoSuchElementException:
                        print(f'Element of index {counter} cannot be found')
                        counter += 1

                result = self.continue_or_close()
                if result:
                    True
                else:
                    break
                
                # reload page
                self.driver.find_element(By.XPATH, '/html/body').send_keys(Keys.HOME)
                time.sleep(0.5)
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[5]/div/span').click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[2]/div/span').click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
                #time.sleep(2)
                self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select/option[{stash}]').click()
                #time.sleep(2)
                # zatwierdzenie wyboru
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/select').click()
                time.sleep(2)
                # wyszukaj
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div[2]/div/div/button[1]').click()
                
                
                
        
        elif start_select == 2:
            
        # go to  manage tab
            self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/menu/a[5]/div/span').click()
            input('This will delete all active trades. Press Enter to continue')
            
            while True:
                delete_counter = 1
                while delete_counter <= 15:
                    time.sleep(0.3)
                    print(f'loop number: {delete_counter}')
                    print()
                    try:
                        self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div[1]/div/div[{delete_counter}]/div[2]/div[2]/div[2]/div[7]/div[1]').click()
                        deleted_item_name = self.driver.find_element(By.XPATH, f'//*[@id="app"]/div[1]/div[2]/div/div/div/div[1]/div/div[{delete_counter}]/div[1]/div/a/h2')
                        print(f'Item: {deleted_item_name.text} deleted')
                        delete_counter += 1
                        
                    except NoSuchElementException:
                        print(f'Element of index {delete_counter} cannot be found')
                        delete_counter += 1
                    
                result = self.continue_or_close()
                if result:
                    True
                else:
                    break
                    
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[2]/div/span').click()    
                time.sleep(2)
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/menu/a[5]/div/span').click()
                time.sleep(2)
    
    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    while True:        
        try:        
            wss_input = int(input('What is the ammount of WSS in HR: '))
            
        except ValueError:
            print('Please input correct value')
            continue
        
        break
    
    login_manager = D2Login(wss_input)
    login_manager.login('https://www.projectdiablo2.com/login','login.txt')
    login_manager.close()