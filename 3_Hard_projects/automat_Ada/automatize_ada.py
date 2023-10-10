from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os


class AduTomat:
    def __init__(self, page, logInto, password):
        self.driver = self.init_driver()
        self.page = page
        self.logInto = logInto
        self.password = password
    
    def init_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        return webdriver.Chrome(options=options)
    
    def login(self):
        self.driver.get(page)  # Otwieramy stronę
        self.driver.maximize_window()
        
    def fill_form(self):
        login_box = self.driver.find_element(By.XPATH, '/html/body/nav/div/div/div[3]/form/div[1]/div/input')
        login_box.send_keys(self.logInto)
        
        password_box = self.driver.find_element(By.XPATH, '/html/body/nav/div/div/div[3]/form/div[2]/div/input')
        password_box.send_keys(self.password, Keys.ENTER)
        time.sleep(2)
    
    def character_select(self):
        character_loop = 1
        while True:
            try:
                character = self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[{character_loop}]/div[1]')
                print(character.text)
                character_loop += 1
            except ValueError:
                print('Please input integer number')
                character_loop += 1
            
            
        '''
        //*[@id="tabs"]/div[1]/div[11]
        //*[@id="tabs"]/div[2]/div[11]
        //*[@id="tabs"]/div[3]/div[11]
        //*[@id="tabs"]/div[4]/div[11]
        //*[@id="tabs"]/div[5]/div[9]
        //*[@id="tabs"]/div[6]/div[9]
        //*[@id="tabs"]/div[15]/div[9]
        '''
    
    
    
    def close(self):
        time.sleep(60)
        self.driver.quit()

if __name__ == '__main__':
    # lokalizowanie pliku txt
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir,'loginFile.txt')
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        if len(lines) == 3:
            page = lines[0].split()[2]
            logInto = lines[1].split()[2]
            password = lines[2].split()[2]
            
            print(f'{page}, {logInto}, {password}')
            
            login_manager = AduTomat(page, logInto, password)
            login_manager.login()
            login_manager.fill_form()
            login_manager.character_select()
            login_manager.close()
            
        else:
            print('Not enough data in login file.')
    

    



