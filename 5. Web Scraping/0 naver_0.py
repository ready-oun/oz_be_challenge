import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = ""
key_word = input("")

# 탐색을 원하는 Url
url = base_url + key_word
# 탐색을 원하는 사이트의 데이터 달라고 요청 
req = requests.get(url, headers=header_user) 