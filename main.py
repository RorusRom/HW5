import requests
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"

headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

session = requests.Session()

for x in range(1, 10):
    print(f"PAGE {x}")
    response = session.get(f"{url}?PAGE={x}", headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_shops = soup.find_all("div", class_="card-body")
        for F in all_shops:
            shop_title = F.find("div", class_="shop-title")
            cash_back = F.find("div", class_="shop-rate")
            formatted_string = f"МАГАЗ: {shop_title.text}, КЕШБЕК: {cash_back.text}"
            print(formatted_string)
