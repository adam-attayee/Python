# the purpose of the app is the scrape an amazon product page and check if price is less than target price.
# if the price is the less than the target price, it sends an email informing the recipeient.

import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "email_address"
MY_APP_PASS = "API_KEY"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US,en;q=0.9',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
           }

url = "https://www.amazon.ca/dp/B000QSNYGI?ref=nb_sb_ss_w_as-reorder_k0_1_8&amp=&crid=2383LS9H1NPVN&sprefix=whey%2Bpro&th=1"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(class_="a-price-whole")
product_price = int(price.get_text().strip('.'))

target_price = 120

if product_price < target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_APP_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject: Product price below target price!! \n\n The product price is {product_price} compared to your "
                                f"target price of {target_price}. Buy now using this link: {url}")
