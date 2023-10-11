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
        print('Wybierz postać:')
        print()
        character_list = []
        # wyszukaj wszystkie postaci na stronie dostepne do zalogowania
        
        characters = self.driver.find_elements(By.CLASS_NAME, 'charName')
        
        for character in characters:
            splitted_character_text = character.text.split()
            character_list.append(splitted_character_text[0])
            
        for index, character in enumerate(character_list, start=1):
            print(f'{index} : {character}')
        
        while True:
            try:
                print()
                select_character = int(input(f'Podaj numer postaci do zalogowania (od 1 do {len(character_list)}): '))
                if 1 <= select_character <= len(character_list):
                    selected_character = self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[{select_character+1}]')
                    # delete_words = selected_character.text.split()
                    # modified_text = ' '.join(delete_words[:-2]) 
                    # print()
                    # print(modified_text)
                    # print()
                    
                    '''Wymyśl jak zostawić taki schemat a jednocześnie usunąc 
                    "Archiwizuj/Przywróć Postać" z ostatniej lini '''
                    
                    print()
                    print(selected_character.text)
                    print()
                    while True:
                        character_check = input('Chcesz zalogować tę postac? [T/N]: ').upper()
                        if character_check == 'T' or 'Y':
                            self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[{select_character+1}]/div[11]').click()
                            print()
                            break
                        
                        elif character_check == 'N':
                            break
                        else:
                            print('Podano niepoprawną wartość. Podaj T/N')
                else:
                    print('Wartość poza zakresem')
                    
            except ValueError:
                print('Podano złą wartość')
                continue
            
            break
        
    def main_menu(self):
        print('Gdzie chcesz przejść w menu:')
        print()
        menu_list = []
        # wyszukaj wszystkie postaci na stronie dostepne do zalogowania
        
        # menu_options = self.driver.find_elements(By.CLASS_NAME, 'srodek_dol')
        menu_options = self.driver.find_elements(By.CSS_SELECTOR,'a.srodek_dol')
        
        for index, menu_option in enumerate(menu_options):
            if index >= 14:
                break
            ref_content = menu_option.get_attribute('ref')
            menu_list.append(ref_content)
            print(f'{index +1} : {ref_content}')

        while True:
            try:
                print()
                select_menu = int(input(f'Podaj numer w menu do przejscia (od 1 do {len(menu_list)}): '))
                if 1 <= select_menu <= len(menu_list):
                    if select_menu == 1:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[1]/img').click()
                    elif select_menu == 2:
                        self.driver.find_element(By.XPATH, f'//*[@id="profilup"]/a/img').click()
                    elif select_menu == 3:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[2]/img').click()
                    elif select_menu == 4:
                        self.driver.find_element(By.XPATH, f'//*[@id="pocztanew"]/a/img').click()
                    elif select_menu == 5:
                        self.driver.find_element(By.XPATH, f'//*[@id="logsnew"]/a/img').click()
                    elif select_menu == 6:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[3]/img').click()
                    elif select_menu == 7:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[4]/img').click()
                    elif select_menu == 8:
                        self.driver.find_element(By.XPATH, f'//*[@id="inncount"]/a/img').click()
                    elif select_menu == 9:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[5]/img').click()
                    elif select_menu == 10:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[6]/img').click()
                    elif select_menu == 11:
                        self.driver.find_element(By.XPATH, f'//*[@id="storiesnew"]/a/img').click()
                    elif select_menu == 12:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[7]/img').click()
                    elif select_menu == 13:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[8]/img').click()
                    elif select_menu == 14:
                        self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[9]/img').click()
              
                
                
                # else:
                #     print('Wartość poza zakresem')
                    
            except ValueError:
                print('Podano złą wartość')
                continue
            
            break            
        

        
      
    
    
    def close(self):
        print('koniec programu')
        time.sleep(50)
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
            
            print('Informacje pobrano z pliku .txt')
            print(f'Page: {page}')
            print(f'Login: {logInto}')
            print(f'Password: {password}')
            
            login_manager = AduTomat(page, logInto, password)
            login_manager.login()
            login_manager.fill_form()
            login_manager.character_select()
            login_manager.main_menu()
            login_manager.close()
            
        else:
            print('Not enough data in login file.')
    

    



