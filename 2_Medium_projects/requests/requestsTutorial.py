import requests
import os

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
comic_path = os.path.join(current_directory, 'comic.png')


# tak można dodawać "payload" do parametrów linku
payload = {'page': 2, 'count': 25}

# -------------------------------------------------------------------
# -----------------------------GET-----------------------------------
# -------------------------------------------------------------------
print()
print('*'*40)
print(' '*18 + 'GET')
print('*'*40)
print()
# r = requests.get('https://imgs.xkcd.com/comics/python.png')

'''strona do testowania różnego rodzaju requestów '''
# r = requests.get('https://httpbin.org/')

r = requests.get('https://httpbin.org/get', params=payload)

#print(r.text)
#print(r.url)
print(f'Get URL: {r.url}')

# print(r)
# print(r.status_code)
# print(r.ok)
'''
Rodzaje statusów

200 - success
300 - redirect
400 - client error
500 - server error
'''

# pobieranie obrazów
# with open (comic_path,'wb') as f:
#     f.write(r.content)


# -------------------------------------------------------------------
# -----------------------------POST----------------------------------
# -------------------------------------------------------------------


print()
print('*'*40)
print(' '*17 + 'POST')
print('*'*40)
print()

payload2 = {'username':'corey','password':'testing'}

r = requests.post('https://httpbin.org/post', data=payload2)
#print(r.text)
r_dict = r.json()
print(r_dict['form'])