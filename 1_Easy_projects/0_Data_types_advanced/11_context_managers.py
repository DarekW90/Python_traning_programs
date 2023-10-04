# Konteksty - context managers - umożliwiają kontrolowanie kontekstu wykonania - np otwieranie i zamykanie plików

import os

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)


def sprawdz_i_utworz_folder(stwórz_folder):
    if not os.path.exists(stwórz_folder):
        os.makedirs(stwórz_folder)
        print(f'Utworzono folder: {stwórz_folder}')
    else:
        print(f'Folder {stwórz_folder} już istnieje.')


class MojKontekst:
    def __init__(self, nazwa_pliku, tryb):
        self.nazwa_pliku = nazwa_pliku
        self.tryb = tryb

    def __enter__(self):
        self.plik = open(self.nazwa_pliku, self.tryb)
        return self.plik

    def __exit__(self, exc_type, exc_value, traceback):
        self.plik.close()


# Użycie kontekstu

stwórz_folder = os.path.join(current_directory, '11_data')
sprawdz_i_utworz_folder(stwórz_folder)

data_directory = os.path.join(current_directory, '11_data\\11_text.txt')
with MojKontekst(data_directory, 'w') as plik:
    plik.write('To jest testowy tekst.')
