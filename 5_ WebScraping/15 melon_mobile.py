from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import time 
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
# 원하는 뷰포인트로 이동 

# Mobile ver. 값을 크롤링하면서 가져오기(굳이 모바일로 직접 접속하지 않아도) : 아이폰 user-agent Googling 
# Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
options = Options()

options.add_argument(f'user-agent={user_agent}') 
options.add_experimental_option('detach', True) 
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service, options=options) 

url = "https://m2.melon.com/index.htm"
driver.get(url)

# mobile ver.은 냅다 광고부터 때리는 게 많아서 현재 주소창이 내가 원하는 url과 다르면 재요청 
time.sleep(0.5)
if driver.current_url != url:
    driver.get(url)

# a 태그를 활용해서 웹페이지의 하이퍼링크를 식별한다. a 태그에 감싸져있는 텍스트를 구별해서 가져올 수 있다. 
driver.find_element(By.LINK_TEXT, "멜론차트").click()
time.sleep(0.5)

mores = driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click() # elements 말고 element 로 하면 하나만 추출됨 
time.sleep(0.5)
# 100위까지 펼쳐진 건가 ?? 뭐지 

melon_chart = driver.find_element(By.CSS_SELECTOR, '#_chartList')
list_100 = melon_chart.find_elements(By. CSS_SELECTOR, '.list_item') # 여러 개 뽑는 거라 element's'

# 초기화
action = ActionChains(driver)

for i in list_100:
    rank = i.find_element(By. CSS_SELECTOR, '.ranking_num a')
    # rank = i.find_element(By. CSS_SELECTOR, '.ranking_num a')
    # rank = i.find_element(By. CSS_SELECTOR, '.ranking_num a')
    # rank = i.find_element(By. CSS_SELECTOR, '.ranking_num a')
    # rank = i.find_element(By. CSS_SELECTOR, '.ranking_num a')
#     change = i.select_one('.ranking_updown a')
#     title = i.select_one('.title.ellipsis a')
#     singer = i.select_one('.name.ellipsis a')
# #    entertainment = 

    action.move_to_element(i).perform() # wtf ? 
    i.find_element(By.CSS_SELECTOR, '.inner > span').click()
    time.sleep(0.5)
    html=driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # 들어가서 들어간 페이지 안의 소스를 html로 받아와서 구조화~! 
    
    driver.back() # 들락날락 ㅎㅎ 
    # action.move_to_element(By.CSS_SELECTOR, '.inner > span').click()

    print(f'순위: {rank.text}')
#     print(f'변동: {change.text}')
#     print(f'제목: {title.text}')
#     print(f'가수: {singer.text}')
    print()

# 모바일 버전에서는 숨겨둔 정보가 많아서 (화면제약때문에) 태그를 깊이 파고 들어야한다.. 
    # 사이트 분석 - 구글링 - GPT help . . .. 

    # KREAM에서 검색하고 싶은 브랜드 개수를 입력하세요: 3
    # => 3개 리스트
    # 프로그램을 실행하면, input으로 값을 받아라 ( var = input => [ ] )

    # 검색을 원하는 브랜드를 입력해주세요 : x3
    # => 입력값 List append 입력 
    # for i input input input => append list => list = ['슈프림', '칼하트', '팔라스'] .send_keys('brand_name')

    # print 만 하는 게 아니라 리스트나 딕셔너리 형태를 만들어서 정보를 담는 겨 : 브랜드, 제품, 가격 .. . . 
    # 사용자의 불편점을 고심해서 여러 기능을 업그레이드해부자 
    # KREAM 을 크롤링하는 이유가 뭘까 ? 