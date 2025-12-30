from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
import re

#Random page web crawler
def getLinks(articleUrl):
    url = f"https://en.wikipedia.org{articleUrl}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        )
    }

    req = Request(url, headers=headers)
    html = urlopen(req)

    bs = BeautifulSoup(html, "html.parser")

    return bs.find("div", {"id": "bodyContent"}) \
             .find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while links:
    newArticle = random.choice(links)["href"]
    print(newArticle)
    links = getLinks(newArticle)