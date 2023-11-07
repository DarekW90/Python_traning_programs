from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os, math


class AduTomat:
    def __init__(self, page, logInto, password):
        self.driver = self.init_driver()
        self.page = page
        self.logInto = logInto
        self.password = password
    
    def init_driver(self):
        options = webdriver.ChromeOptions()
        #options.headless = True
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        #options.add_argument('--no-sandbox')
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
        # print('Wybierz postać:')
        # print()
        # character_list = []
        # wyszukaj wszystkie postaci na stronie dostepne do zalogowania
        
        # characters = self.driver.find_elements(By.CLASS_NAME, 'charName')
        
        # for character in characters:
        #     splitted_character_text = character.text.split()
        #     character_list.append(splitted_character_text[0])
        
        ''' dodano dla testów '''
        self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[2]').click()
        print()
        print('-'*20)
        print('Zatwierdź ENTER jeśli walka nie jest w toku')
        input('-'*20)
        
        
        ''' wyłączono do testów'''
        '''
        while True:    
        
            for index, character in enumerate(character_list, start=1):
                print(f'{index} : {character}')
                
            
               
            print()
            select_character = int(input(f'Podaj numer postaci do zalogowania (od 1 do {len(character_list)}): '))
            if 1 <= select_character <= len(character_list):
                #selected_character = self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[{select_character+1}]')
                selected_character = self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[2]').click()
                
                #Wymyśl jak zostawić taki schemat a jednocześnie usunąc 
                # Archiwizuj/Przywróć Postać z ostatniej lini 
                
                print()
                print(selected_character.text)
                print()
            
                character_check = input('Chcesz zalogować tę postac? [T/N]: ').upper()
                if character_check in ['T', 'Y']:
                    self.driver.find_element(By.XPATH, f'//*[@id="tabs"]/div[{select_character+1}]/div[11]').click()
                    print()
                    break
                
                elif character_check == 'N':
                    continue
                else:
                    print('Podano niepoprawną wartość. Podaj T/N')
            else:
                print('Wartość poza zakresem')
        '''        
        
    def main_menu(self):
        # print('Gdzie chcesz przejść w menu:')
        # print()
        menu_list = []
        # wyszukaj wszystkie postaci na stronie dostepne do zalogowania
        
        menu_options = self.driver.find_elements(By.CSS_SELECTOR,'a.srodek_dol')
        
        for index, menu_option in enumerate(menu_options):
            if index >= 14:
                break
            ref_content = menu_option.get_attribute('ref')
            link_content = menu_option.get_attribute('href')
            menu_list.append((ref_content, link_content))
            
            #print(f'{index +1} : {ref_content}')
        while True:
            try:
                print()
                ''' wyłączone do testów '''
                #select_menu = int(input(f'Podaj numer w menu do przejścia (od 1 do {len(menu_list)}): '))
                #element_to_click = menu_list[select_menu - 1]
                element_to_click = menu_list[11]
                link_content = element_to_click[1]
                self.driver.get(link_content)
            except ValueError:
                print("Wprowadź poprawną liczbę.")
            break            
        
    def organizacje_i_rody(self):
        # organizacja walczy o ...
        #time.sleep(2)
        fight_info = self.driver.find_element(By.XPATH, f'//*[@id="component_content"]/div[2]/h1[1]')
        print(fight_info.text)
        # organizacja wygrała do tej pory XXX walk
        fight_info_2 = self.driver.find_element(By.XPATH, f'//*[@id="component_content"]/div[2]/h1[3]')
        print('='*40)
        print(fight_info_2.text)
        # weź udział
        join_fight = self.driver.find_element(By.XPATH, f'//*[@id="component_content"]/div[2]/h1[4]/a')
        adres_url = join_fight.get_attribute('href')
        # Wyświetlenie adresu URL
        print('='*40)
        print(adres_url)
        print('='*40)
        self.driver.get(adres_url)
        # dodano dla przyspieszenia
        
        #join_fight.click()
        # #print(join_fight.text)
        # while True:
        #     try:
        #         joining = input('Chcesz dołączyć (T/N)? ').upper()
        #         if joining in ['T', 'Y']:
        #             join_fight.click()
        #             break
        #         elif joining == 'N':
        #             print('Powrót do strony głównej')
        #             self.driver.find_element(By.XPATH, f'//*[@id="top_menu_content"]/a[1]/img').click()
        #             self.main_menu()
        #             break
        #         else:
        #             print('Podano złą wartość')
        #     except ValueError:
        #         print('Podano złą wartość (T/N)')
    
    def menu_walk(self):
        while True:
            start_total_time = time.time()
            check_pa = self.driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div[6]/div[2]/div[1]/div[3]/div[4]/span[1]')
            print(f'Posiadasz dostępnych {check_pa.text} PA')
            int_check_pa = int(check_pa.text)
            print(f'Pozwala to na stoczenie >>> {math.floor(int_check_pa/10)}')
            print()
            #battle_count = int(input('Ile chcesz stoczyć walk : '))
            #great_loop = int(input('Ile pętli? Jedna pętla to 32 walki! : '))
            
            # dodano dla przyspieszenia
            great_loop = 111
            
            little_loop = 1
            
            while little_loop <= great_loop:
                
                great_loop_start = time.time()
                panel_boczny = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[1]/a[2]')
                panel_boczny.click()
                time.sleep(0.1)
                fill_pa = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[2]/div/div[1]/input[2]')
                fill_pa.click()
                    
                battle_count = 32
                
                battle_loop = 1
                while battle_loop <= battle_count:
                    start_battle_time = time.time()
                    
                    print(f'Great loop : {little_loop} z {great_loop}')
                    print(f'Walka {battle_loop} z {battle_count}')
                    print()
                    # ------------------------------------------
                    # Tutaj delay na załadowanie okna startowego
                    # ------------------------------------------
                    # !!!!!!!! NIE ZMIENIAĆ !!!!!!!!
                    # ------------------------------------------
                    #time.sleep(2) #works fine
                    time.sleep(0.7)
                    # ------------------------------------------
                    # heal
                    heal = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[1]/a[5]')
                    #print('heal')
                    heal.click()
                    
                    # repair
                    repair = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div[1]/a[6]')
                    #print('repair')
                    repair.click()
                    
                    help_for_pa = self.driver.find_element(By.XPATH, f'//*[@id="component_content"]/div[1]/hgroup/div/form[1]/input')
                    help_for_pa.click()
                    
                    # ------------------------------------------
                    # tutaj delay na załadowanie planszy walki 
                    # ------------------------------------------
                    # !!!!!!!! NIE ZMIENIAĆ !!!!!!!!
                    # ------------------------------------------
                    #time.sleep(2) #works fine
                    print('ładowanie planszy')
                    time.sleep(0.5)
                    print('załadowało planszę')
                    # ------------------------------------------
                    
                    summon = self.driver.find_element(By.XPATH, f'//*[@id="player_1"]/div[6]/img[5]')
                    #print('przywołanie szkieletu')
                    summon.click()
                    
                    # ------------------------------------------
                    # tutaj delay na przeliczenie ilości przeciwników
                    # ------------------------------------------
                    time.sleep(0.15)
                    # ------------------------------------------
                    
                    wykryto_wrogow = 0
                    
                    for x in range(2,20):
                        element_name = f'player_{x}'
                        elements = self.driver.find_elements(By.XPATH, f'//*[@id="{element_name}"]/div[2]')
                        wykryto_wrogow += len(elements)
                        
                    print(f"Liczba znalezionych elementów 'player_x': {wykryto_wrogow}")
                    
                    #wykryto_wrogow = 15
                    
                    # input('przerwij program ręcznie')
                    
                    target_count = 1
                    liczba_wrogow = ((wykryto_wrogow*2)-1)
                    while target_count <= liczba_wrogow:
                        #print(f'Numer wroga: {target_count}')
                        try:
                            atak_aoe = self.driver.find_element(By.XPATH, f'/html/body/div/div[3]/div[5]/div[4]/div[{target_count}]/div[6]/img[1]')
                            atak_aoe.click()
                            
                            # ------------------------------------------
                            # Tutaj delay na załadowanie się "ludzika" 
                            # ------------------------------------------
                            #time.sleep(1) # works fine
                            '''
                        
            Tutaj ustawiasz opóźnienie na załadowanie ludzika
                            '''
                            time.sleep(0.3)
                            # ------------------------------------------
                            
                            try:
                                attack_head = self.driver.find_element(By.XPATH,
                                                                f"/html/body/div/div[3]/div[5]/div[4]/div[{target_count}]/div[1]/div[1]")
                                attack_head.click()
                                print('head shot')
                                
                                # ------------------------------------------
                                # Tutaj delay po kliknięciu ataku w głowę
                                # ------------------------------------------
                                #time.sleep(1) works fine
                                '''
                Tutaj ustawiasz opóźnienie po ataku na głowe 
                                '''
                                
                                time.sleep(0.3)
                                # ------------------------------------------
                                
                            except NoSuchElementException:
                                #print(f"nie znaleziono celu - głowa: dla przeciwnika nr: {target_count}")
                                pass
                                
                        except NoSuchElementException:
                            
                            # ------------------------------------------
                            # Tutaj delay na wyszukanie następnego celu
                            # ------------------------------------------
                            #time.sleep(1)
                            # ------------------------------------------
                            
                            #print(f'brak celu: {target_count}')
                            target_count += 1
                            
                    # ------------------------------------------
                    # Tutaj delay na rozpoczęcie nowej rundy - klik Wyjdz z walki
                    # ------------------------------------------
                    #time.sleep(0.2) # works fine
                    time.sleep(0.25)
                    # ------------------------------------------
                    quit_battle = self.driver.find_element(By.XPATH, f'//*[@id="fight_middleside"]/div[1]/div[1]/a')
                    quit_battle.click()
                    
                    # ------------------------------------------
                    # czasomierz
                    # ------------------------------------------
                    stop_battle_time = time.time()
                    total_time = stop_battle_time - start_battle_time
                    round_battle_time = round(total_time,2)
                
                    print()
                    print('-'*20)
                    print(f'Wykonanie walki nr {battle_loop} w {round_battle_time} sekund')
                    print('-'*20)
                    print()
                    # ------------------------------------------
                    
                    battle_loop += 1
                # ------------------------------------------
                # czasomierz
                # ------------------------------------------
                stop_total_time = time.time()
                total_time = stop_total_time - start_total_time
                round_total_time = round(total_time,2)
            
                print()
                print('-'*20)
                print(f'Wykonanie {battle_count} walk w {round_total_time} sekund')
                print('-'*20)
                print()
                # ------------------------------------------
                
                little_loop += 1
                
            great_loop_stop = time.time()
            great_loop_time = great_loop_start - great_loop_stop
            print(f'Wykonano {great_loop} walk w czasie {great_loop_time}')
            
            
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
            login_manager.organizacje_i_rody()
            login_manager.menu_walk()
            login_manager.close()
            
        else:
            print('Not enough data in login file.')
    

    



