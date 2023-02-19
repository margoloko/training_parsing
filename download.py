from bs4 import BeautifulSoup as BS
import requests_cache
import re


DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BS(response.text, 'lxml')
    #main_tag = soup.find('div', {'role': 'maim'})
    table_tag = soup.find('table', {'class': 'docutils'})
    a4_tag = table_tag.find('a', {'href':re.compile(r'.+pdf-a4\.zip$')})
    
    
    
    print(a4_tag)