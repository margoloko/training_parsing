import requests_cache
import re

from pathlib import Path
from bs4 import BeautifulSoup as BS
from urllib.parse import urljoin


BASE_DIR = Path(__file__).parent
DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BS(response.text, 'lxml')
    #main_tag = soup.find('div', {'role': 'maim'})
    table_tag = soup.find('table', {'class': 'docutils'})
    a4_tag = table_tag.find('a', {'href':re.compile(r'.+pdf-a4\.zip$')})
    a4_link = a4_tag['href']    
    archive_url = urljoin(DOWNLOADS_URL, a4_link)
    filename = archive_url.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    response = session.get(archive_url)
    with open(archive_path, 'wb') as file:
        file.write(response.content)
    
    print(filename)