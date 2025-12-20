from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    #throws if server dne
    except AttributeError as e:
        return None
    return title

if __name__ == '__main__':
    title = getTitle('http://pythonscraping.com/pages/page1.html')
    if title == None:
        print('Title not found')
    else:
        print(title)

