import requests
from bs4 import BeautifulSoup
import time
import re
import mysql.connector


base_url = "https://reiwa.com.au/for-sale/broadwood+karlkurla+binduli+hannans+kalgoorlie+boulder+fimiston+south-boulder+victory-heights/?includesurroundingsuburbs=true&sortby=listdate&page="
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
                    address_id = full_link.rstrip('/').split('-')[-1]
                    

                    if(int(price) < 450000):

                        print(f"Address: {address}, Price: {price}, Link: {full_link}")
                        conn = mysql.connector.connect(
                        host="192.168.1.108",  
                        user="myuser",
                        password="mypassword",
                        database="Houses_Scrapper"
                        )

                        cursor = conn.cursor()

                        cursor.execute("Select * from Houses_List where house_id="+address_id)

                        result = cursor.fetchone()
                        
                        if result:
                            print(f"House with ID {address_id} already exists.")
                        else:
                            sql = "INSERT INTO Houses_List (address, house_id, price, web_url) VALUES (%s, %s, %s, %s)"
                            values = (address, address_id, price, full_link)

                            cursor.execute(sql, values)
                            conn.commit()
                            print(f"Inserted house with ID {address_id}.")

                        cursor.close()
                        conn.close()

        else:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            time.sleep(1)

    except Exception as e:
        print(f"Error scraping page {page}: {e}")
