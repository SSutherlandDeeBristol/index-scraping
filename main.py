import urllib.request
from bs4 import BeautifulSoup
from collections import defaultdict

indices = defaultdict(list)

def extract_market_data(soup):
    trs = soup.find_all('tr')

    for tr in trs:
        th = tr.find('th')
        index_name = ''

        div1 = th.find('div')
        if div1 is not None:
            div2 = div1.find('div')
            if div2 is not None:
                a = div2.find('a')
                if a is not None:
                    spans = a.find_all('span')
                    if spans is not None:
                        index_name = spans[0].get_text()

        tds = tr.find_all('td')
        value = ''

        if len(tds) > 0:
            td1 = tds[1]
            if td1 is not None:
                div = td1.find('div')
                if div is not None:
                    value = div.get_text()

                if index_name is not '':
                    indices[index_name] = value

def soupify_page():
    with open("webpage.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    #soup = BeautifulSoup('webpage.html', 'html.parser')
    return soup

def download_page():
    url = 'https://www.bbc.co.uk/news/business/market-data'

    urllib.request.urlretrieve(url, 'webpage.html')

if __name__ == '__main__':
    download_page()
    soup = soupify_page()
    extract_market_data(soup)

    print(str(indices))