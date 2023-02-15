from bs4 import BeautifulSoup as BS
import requests_cache


MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    soup = BS(response.text, 'lxml')    
    sidebar = soup.find('div', attrs = {'class':'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')
    print(ul_tags)