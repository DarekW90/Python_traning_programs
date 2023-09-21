import pandas as pd
import os

df1 = pd.read_csv('G:\\.Cwiczenia\\BackEnd\\Python_portfolio\\3_Hard_projects\\NetScrapping\\More_ambitious_project\\Scraper_ps\\data\\playstation_data.csv', sep=';')
df2 = pd.read_csv('G:\\.Cwiczenia\\BackEnd\\Python_portfolio\\3_Hard_projects\\NetScrapping\\More_ambitious_project\\Scraper_xbox\\data\\xbox_data.csv', sep=';')


zestawienie = pd.merge(df1, df2, on='Game', suffixes=('_playstation', ('_xbox')))
zestawienie = zestawienie.drop(columns=['Status_playstation','Status_xbox'])
# print(zestawienie.columns)
zestawienie['Price_playstation'] = zestawienie['Price_playstation'].str.replace('ZŁ', '').str.replace('.', ',')
zestawienie['Price_xbox'] = zestawienie['Price_xbox'].str.replace('ZŁ', '').str.replace('.', ',')

print(zestawienie)

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
data_directory = os.path.join(current_directory, 'data')
os.makedirs(data_directory, exist_ok=True)

csv_path = os.path.join(data_directory, 'pandas_data.csv')
zestawienie.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')