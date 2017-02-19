# If uncommented ewerything - still be working, but wuth opening webpage in Chrome
import bs4 as bs
import time
import urllib.request
from urllib.parse import quote

# from selenium import webdriver
# chrome_path = r'C:\Users\Pavlo\Desktop\Python\chromedriver_win32\chromedriver.exe'

BASE_URL = 'http://www.google.com.ua/search?q=dog'
PAGES_URL = '&hl=ua&start='
ENDING = '&gws_rd=ssl'

# driver = webdriver.Chrome(chrome_path)
# driver.get(BASE_URL)


def get_request():
    example_search = input('Enter your google request: ')
    # example_search = 'dog'
    encoded = quote(example_search)
    return encoded


# def number_of_links():
#     number_links = input('How many links do you want ?: ')
#     return int(number_links)


def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Chrome'})
    html = urllib.request.urlopen(req).read()
    return html
    # return driver.page_source


def parse(html):
    soup = bs.BeautifulSoup(html, 'lxml')
    div = soup.find_all('cite')

    links = []
    for i in div:
        link = i.text
        encoded = link.encode('utf-8')
        decoded = encoded.decode('unicode-escape')
        links.append(decoded)
    return links


def get_page_count(html):
    soup = bs.BeautifulSoup(html, 'lxml')
    table = soup.find('table', attrs={'id': 'nav'})
    for tr in table:
        page_count = [i.text for i in tr][-2]
        return int(page_count)


def main():
    request = get_request()
    # number_links = number_of_links()
    links = []
    number = 0

    page_count = get_page_count(get_html(BASE_URL + request + PAGES_URL + str(number*10) + ENDING))
    for page in range(0, page_count):
        links.extend(parse(get_html(BASE_URL + request + PAGES_URL + str(number*10) + ENDING)))
        number += 1

    number = 0

    for href in links:
        try:
            number += 1
            print(number, href)
        except Exception:
            print('Sorry...that is give an error')


    time.sleep(120)


if __name__ == '__main__':
    main()
