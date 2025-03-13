# Należało pobrać chromeDriver 
# Używane komendy:
#pip install selenium
#pip freeze > requirements.txt
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Home():

    def __init__(self, header_name, price, price_m2):
        self.header_name = header_name
        self.price = price
        self.price_m2 = price_m2

    def return_data(self):
        return {
            'header_name': self.header_name,
            'price': self.price,
            'price_for_m2': self.price_m2
        }

def pobranie_postow():
    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing')

    post_loaded = expected_conditions.presence_of_element_located((By.TAG_NAME, 'article'))
    WebDriverWait(driver, 15).until(post_loaded)

    slownik = {}
    i = 1

    for post in driver.find_elements(By.TAG_NAME, 'article'):
        tytul = post.find_element(By.CLASS_NAME, 'css-16vl3c1').text
        cena = post.find_element(By.CLASS_NAME, 'css-afwkhs').text
        cena_m2 = post.find_element(By.XPATH, ".//dt[text()='Cena za metr kwadratowy']/following-sibling::dd[1]/span").text
        
        home = Home(tytul, cena, cena_m2)
        slownik[f'oferta_{i}'] = home
        i += 1

    with open("home.csv", mode="w", newline="", encoding="utf-8") as plik:
        writer = csv.writer(plik)
        writer.writerow(["header_name", "price", "price_m2"]) #Nagłówki
        
        #Wypisanie elementów słownika
        for key, oferta in slownik.items():
            print(key, oferta.return_data())
            writer.writerow([oferta.header_name, oferta.price, oferta.price_m2])


    driver.stop_client()

if __name__ == '__main__':
    pobranie_postow()