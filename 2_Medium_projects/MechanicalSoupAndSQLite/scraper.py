# https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions

import mechanicalsoup, sqlite3, os
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions'
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)


''' extract table headers '''
th = browser.page.find_all('th', attrs={'class': 'table-rh'})
distribution = [value.text.replace('\n', '') for value in th]
#print(distribution.index('Zorin OS'))
distribution = distribution[:98]
# print(distribution)

''' extract table data '''
td = browser.page.find_all('td')
columns = [value.text.replace('\n', '') for value in td]
columns = columns[6:1084]

column_names = ['Founder',
                'Maintainer',
                'Initial_Release_Year',
                'Current_Stable_Version',
                'Security_Updates',
                'Release_Date',
                'System_Distribution_Commitment',
                'Forked_From',
                'Target_Audience',
                'Cost',
                'Status']

dictionary = {'Distribution': distribution}

for idx, key in enumerate(column_names):
    # dictionary['Founder']=columns[0:][::11]
    dictionary[key] = columns[idx:][::11]

''' data frame '''
df = pd.DataFrame(data=dictionary)
#print(df)

# print(columns.index('AlmaLinux Foundation'))
# print(columns.index('Binary blobs'))
# print(columns)

''' select every 11th item '''
# columns[0:][::11]
# columns[1:][::11]
# columns[2:][::11]
# columns[3:][::11]


''' insert data into a database '''

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
data_base_path = os.path.join(current_directory, 'linux_distro.db')

connection = sqlite3.connect(data_base_path)

cursor = connection.cursor()

cursor.execute('CREATE TABLE linux (Distribution, ' + ','.join(column_names) + ')')
for i in range(len(df)):
    cursor.execute('INSERT INTO linux values (?,?,?,?,?,?,?,?,?,?,?,?)', df.iloc[i])
    
connection.commit() # permanent save !!!

connection.close()