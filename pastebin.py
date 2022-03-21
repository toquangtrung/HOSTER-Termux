import requests
from bs4 import BeautifulSoup

def scrape(url):
    # url = "https://pastebin.com/vURBd340"
    #url = "https://pastebin.com/FbHZjHkd"
    url_list = []
    content = requests.get(url)

    soup = BeautifulSoup(content.text,"html.parser")

    raw = soup.find_all("textarea",class_="textarea")

    for p in raw:
        url_list.append(p.text.split())
    return url_list[0]

    