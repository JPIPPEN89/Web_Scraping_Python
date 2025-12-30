from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def get_page(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('The Server returned an HTTP error')
    except URLError as e:
        print('The server could not be found')
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None

    title = bsObj.find_all('title')
    print('PAGE TITLE: ')
    for t in title:
        print(f'{t}\n')

    h1_titles = bsObj.find_all('h1')

    print('H1 HEADERS: \n')
    for h in h1_titles:
        print(f'-  {h}\n')

    print('LINKS FOUND:\n')

    for link in bsObj.find_all('a'):
        if 'href' in link.attrs:
            att = link.attrs['href']
        print(f'Text: {link.getText()}  |  URL: {att}')

get_page('https://news.ycombinator.com/')




