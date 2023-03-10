import csv
import requests
from bs4 import BeautifulSoup as bs

count = 0

def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text

def get_last_page(html: str) -> int:
    soup = bs(html, 'lxml')
    pages = soup.find('div', class_='pages fl').find_all('a', class_='pages-item')
    last_page = pages[-1].get('data-ci-pagination-page')
    return int(last_page)

def get_data(html:str) -> list:
    soup = bs(html, 'lxml')
    catalog = soup.find('div', class_ = 'catalog-list')
    cars = catalog.find_all('a', class_ = 'catalog-list-item')
    result = []
    for car in cars:
            
        name = car.find('span', class_ = 'catalog-item-caption').text.strip()
        try:
            img = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            img = 'No picture'
        price = car.find('span', class_ = 'catalog-item-price').text
        desc1 = car.find('span', class_ = 'caption-year').text.strip()
        desc2 = car.find('span', class_ = 'catalog-item-mileage').text.strip()
        desc3 = car.find('span', class_ = 'catalog-item-descr').text.strip()
        description = f'{desc1} {desc2} {desc3}'

        data = {
            'name': name,
            'price': price,
            'description': description,
            'img': img
        }

        result.append(data)

    return result

def write_to_csv(data:dict) -> None:
    with open('cars_pars.csv', 'a') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        global count

        for car in data:
            count += 1
            writer.writerow ({
                '#': count,
                'Name': car['name'],
                'Price': car['price'],
                'Description': car['description'],
                'Image':car['img']
            })

def prepare_csv() -> None:
    with open ('cars_pars.csv', 'w') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '#': '#',
            'Name': 'Name',
            'Price': 'Price',
            'Description': 'Description',
            'Image':'Image'
            })

def main():
    i = 1
    prepare_csv()
    while True:
        url = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        last_page = get_last_page(html)
        data = get_data(html)
        write_to_csv(data)
        print(f'???????????????? {i}/{last_page} ????????????????!')
        if i == 94:
            break
        i += 1
        

main()