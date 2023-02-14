from tqdm import tqdm
from time import sleep
import requests_cache
import requests

URL = 'http://httpbin.org/delay/3'

if __name__ == '__main__':
    for i in tqdm(range(3), desc='"Загрузка с сервера"'):
        requests.get(URL)
        
    session = requests_cache.CachedSession()
    #session = requests_cache.CachedSession('http_cache', backend='filesystem')
    session.cache.clear()

        
    
    for i in tqdm(range(3), desc='3агрузка из кеша'):
        session.get(URL)
        

