from selenium import webdriver
from bs4 import BeautifulSoup 
import time

url = "https://naver.com"

# 셀레니움은 웹브라우저를 통해서 결과물을 가져다준다 ?! 

driver = webdriver.Chrome()
driver.get(url) #url에 있는 드라이버 주소를 갖다준다 ? 
time.sleep(4) # 4s 시간 조절 

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one('#query')
print(query)
