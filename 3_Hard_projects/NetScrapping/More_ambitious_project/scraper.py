# https://www.mediaexpert.pl/smartfony-i-zegarki/smartfony?page=1
import mechanicalsoup
import os
import pandas as pd


page = 0
data = {'Model': [], 'Price': []}

while page < 5:
    url = f'https://www.amazon.pl/s?i=electronics&bbn=20657432031&rh=n%3A26955202031&fs=true&page={page}&qid=1695143308&ref=sr_pg_6'
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)

    # extract titles
    models = browser.page.find_all(
        'span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})
    prices = browser.page.find_all('span', attrs={'class': 'a-offscreen'})

    for model, price in zip(models, prices):
        # model_text = model.text
        # price_text = price.text
        data['Model'].append(model.text)
        data['Price'].append(price.text)

    page += 1
    print(f"Current page: {page}")

df = pd.DataFrame(data)
print(df)
