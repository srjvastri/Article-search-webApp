#import urllib.request
import json
import requests
endpoint = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
key = 'xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei'
url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=' + key
r = requests.get(url)
json_data = r.json()
5
