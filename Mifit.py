import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com.br/Smartwatch-Amazfit-Xiaomi-Huami-Internacional/dp/B076WRDKQM/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1VZFLO9LTOMA6&keywords=smartwatch&qid=1565300043&s=gateway&sprefix=smartw%2Caps%2C221&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    convert_price = int(price[2:5])

    if(convert_price > 348):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('lucastavaresa95@gmail.com', 'dgxzxvwovnjhliau')

    subject = 'Price is great!'
    body = 'Check this link! https://www.amazon.com.br/Smartwatch-Amazfit-Xiaomi-Huami-Internacional/dp/B076WRDKQM/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1VZFLO9LTOMA6&keywords=smartwatch&qid=1565300043&s=gateway&sprefix=smartw%2Caps%2C221&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'lucastavaresa95@gmail.com',
        'lucastavaresa95@gmail.com',
        msg
    )
    print('Email sent!')

    server.quit()

check_price()


