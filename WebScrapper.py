import requests
from bs4 import BeautifulSoup
import time
import re

base_url = "https://reiwa.com.au/for-sale/broadwood+karlkurla+binduli+hannans+kalgoorlie+boulder+fimiston+south-boulder+victory-heights/?includesurroundingsuburbs=true&sortby=default&page="
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

for page in range(1, 25):
    url = base_url + str(page)
    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            property_cards = soup.find_all('a', class_='p-card__details u-block')
            
            if (property_cards == []):
                break

            for card in property_cards:
                href = card.get('href')
                price_tag = card.find('p', class_='heading h4 sk-item')

                if href and price_tag:
                    full_link = 'https://reiwa.com.au' + href
                    raw_price = price_tag.get_text(strip=True)
                    price = re.sub(r'[^\d]', '', raw_price)

                    path = href.strip('/')
                    path = re.sub(r'-\d+$', '', path)
                    address = path.replace('-', ' ')
                    address = address.title()
                    print(f"Address: {address}, Price: {price}, Link: {full_link}")

        else:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            time.sleep(1)

    except Exception as e:
        print(f"Error scraping page {page}: {e}")