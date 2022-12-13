
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import csv

url = 'https://www.kivano.kg/mobilnye-telefony'

headers = {
        'accept':'*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}

page = requests.get(url, headers=headers)
src = page.text

#with open('index.html', 'a') as f:
    #f.write(src)

#with open('index.html', 'r') as r:
    #src = r.read()
    #print(src)


soup = BeautifulSoup(src, 'lxml')

finder = soup.find_all('div', class_='item product_listbox oh')
phones = []

for p in finder:
    phones.append({
        'Names': p.find('div', class_='listbox_title oh').get_text(strip=True),
        'Info': p.find('div', class_='product_text pull-left').get_text(strip=True),
        'Price': p.find('div', class_='listbox_price text-center').get_text(strip=True)
    }

)
with open('phone.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(
         ("Название",
          "Описание",
          "Цена"
        )
)


for i in range(len(phones)):
    names = phones[i]['Names']
    info = phones[i]['Info']
    price = phones[i]['Price']

    with open('phone.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (names,
             info,
             price
    )
)