#import requests
from tqdm import tqdm
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
    result = []
    for li in tqdm(get_li):        
        version_a_tag = li.find('a')
        href = version_a_tag['href']
        ssil = urljoin(WHATS_NEW_URL, href)
        session =requests_cache.CachedSession()
        response = session.get(ssil)
        response.encoding = 'utf-8'
        soup_v = BS(response.text, 'lxml')
        h1 = soup_v.find('h1')
        dl = soup_v.find('dl')
        dl_text = dl.text.replace('\n', ' ')
        result.append((ssil, h1.text, dl_text))
        # Печать списка с данными.
        for row in result:
        # Распаковка каждого кортежа при печати при помощи звездочки.
            print(*row)
    
    
    #section id='what-s-new-in-python
    #div class="toctree-wrapper compound"
    #li class="toctree-l2"
