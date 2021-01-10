import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?acampID=0&cmp=RMX&loc=Hatch&ref=198&skuId=6429442'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    button = soup2.find("div",{"class":"fulfillment-add-to-cart-button"}).find('div').getText().strip()
    if(button != 'Sold Out'):
        send_mail()



def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("cristhianswork@gmail.com", "thisisnew.")
    subject = "HEYYYYY GET THE RTX ITS IN BESTBUY"
    body = " GET THE GRAPHICS CARD NOOOOW  https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?acampID=0&cmp=RMX&loc=Hatch&ref=198&skuId=6429442"
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
    time.sleep(43200)
