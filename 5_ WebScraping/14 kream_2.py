from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 
from bs4 import BeautifulSoup

# 키보드 관련 동작과 관련된 기능을 쓰기 위한 패키지 불러오기 
from selenium.webdriver.common.keys import Keys # 대소문자 구분

# 클래스, 아이디, css_selector를 위한 패키지
from selenium.webdriver.common.by import By 
# 대소문자 구분 

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options = Options()

options.add_argument(f'user-agent={user_agent}') 
options.add_experimental_option('detach', True) 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service, options=options) 

url = "https://kream.co.kr"
driver.get(url)
#  time.sleeo(0.5)

# 돋보기 클릭해서 후드만, 브랜드, 즉시구매가 추출해보자 

# 돋보기 클릭을 학 ㅗ싶다... 그거를 위한 클래스를 가져오자 ! 
# search_btn_box 

driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click() 
#css에서 구분하는 방법을 그대로 가져와서 클릭이벤트함수

# driver.quit()

