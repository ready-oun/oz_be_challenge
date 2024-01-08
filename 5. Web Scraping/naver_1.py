import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

#get 방식 : 서버에게 리소스(자원)를 요청, 데이터를 수신하는 기능 
req = requests.get(url)
print(req) #run code 시, command not found가 뜬다 >> run code가 아닌 >파이썬 파일 실행<을 해야 한다. response 200이 뜨면 정상. 