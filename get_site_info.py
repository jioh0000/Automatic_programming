import requests
from bs4 import BeautifulSoup

url = "https://mario-tv.com/bbs/page.php?hid=livetv"

response = requests.get(url)
print(response)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    schedule = soup.select_one("body > div > div > div > table > tbody > tr > td")
    print(soup)
    print(schedule)