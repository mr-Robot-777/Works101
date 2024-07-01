from bs4 import BeautifulSoup
import requests

number = input('Введите номер детали: ')
# Пример 06a905115d
URL = f'https://autopiter.ru/goods/{number}'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0'
}


def get_html(url, params=''):
    r = requests.get(url, params=params) # (url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='IndividualTableRow__descriptionColumn___dFBnQ').text
    print(items)


html = get_html(URL)
get_content(html.text)



