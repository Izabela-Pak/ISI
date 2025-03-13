#Do działania tego należało zainstalować "pip install beautifulsoup4" oraz "pip install requests"
#BeautifulSoup służy do analizowania (parsowania) gotowego HTML
#Do pobrania treści strony służy biblioteka requests.

import requests
from bs4 import BeautifulSoup

def pobieranie_linkow(url: str)-> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        print(link.get('href'))

if __name__ == '__main__':
    url = 'https://www.empik.com/nie-ma-tego-zlego-mortka-marcin,p1257181764,ksiazka-p'
    pobieranie_linkow(url)