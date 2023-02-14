#import requests
import requests_cache

URL = 'https://docs.python.org/3/whatsnew/'

session = requests_cache.CashedSession()
print(session.get(URL))