import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-1-8GHz-dual-core-Intel/dp/B07211W6X2/ref=sr_1_1?crid=1AL6PTE58V6E9&keywords=macbook+air&psr=EY17&qid=1576272608&s=cyber-monday&smid=ATVPDKIKX0DER&sprefix=macbook%2Ccyber-monday%2C155&sr=1-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text().strip()
    price = soup2.find(id="priceblock_dealprice").get_text().strip()
    converted_text = float(price[1:7])
    if(converted_text > 500):
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("cristhianswork@gmail.com", "thisisnew.")
    subject = "price fell down"
    body = "check amazon link https://www.amazon.com/Apple-MacBook-1-8GHz-dual-core-Intel/dp/B07211W6X2/ref=sr_1_1?crid=1AL6PTE58V6E9&keywords=macbook+air&psr=EY17&qid=1576272608&s=cyber-monday&smid=ATVPDKIKX0DER&sprefix=macbook%2Ccyber-monday%2C155&sr=1-1"
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail(
        "cristhianswork@gmail.com",
        "christiandevwork@gmail.com",
        msg
    )
    print("hey email has been sent!")
    server.quit()


while(True):
    check_price()
    time.sleep(60*60)
