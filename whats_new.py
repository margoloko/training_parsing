#import requests
import requests_cache
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin


WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'
    #print(response.text)


    soup = BS(response.text, features='lxml')
    get_section = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    get_div = get_section.find('div', attrs={'class': "toctree-wrapper compound"})
    get_li = get_div.find_all('li', attrs={'class': "toctree-l2"})
    #print(get_li[0].prettify())
    for li in get_li:
        version_a_tag = li.find('a')
        href = version_a_tag['href']
        ssil = urljoin(WHATS_NEW_URL, href)
        print(ssil)
    
    
    #section id='what-s-new-in-python
    #div class="toctree-wrapper compound"
    #li class="toctree-l2"
