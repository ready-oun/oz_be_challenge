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
#  time.sleep(0.5)

# 돋보기 클릭해서 후드만, 브랜드, 즉시구매가 추출해보자 

# 돋보기 클릭을 학 ㅗ싶다... 그거를 위한 클래스를 가져오자 ! 
# search_btn_box 

#css에서 구분하는 방법을 그대로 가져와서 클릭이벤트함수
driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click() 
time.sleep(1)

# 검색창에 입력 // 클래스 두 개 구분 위해 앞뒤로 . 삽입
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

# Enter 치기 
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

# 이전에 배운 마우스 휠 내리는 거 말고 '키보드'로 스크롤 내리기
# 한 20회만 해보자 
for i in range(20):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

    # 1번 내려갈 때 스크린샷 찍는 기능, 괄호 안에 경로 넣어서 저장할 경로 지정 & supreme.png로 저장
    driver.save_screenshot("/Users/robin/Desktop/oz_be_challenge/5. Web Scraping/Kream_img/supreme"+str(i)+".png")
    time.sleep(0.3)


# html 코드를 가져와서 구조화 
html = driver.page_source 
soup= BeautifulSoup(html, "html.parser") 

items = soup.select(".item_inner")

# 클래스 통해 후드만 추출하기 : translated_name  //추출한 글자 안에 후드가 있으면 출력하게!

num = 1
for i in items:
    product_name = i.select_one(".translated_name")

    if "후드" in product_name.text:
        product_brand = i.select_one(".product_info_brand.brand")
        product_name_hood = i.select_one(".translated_name")
        product_price = i.select_one(".amount")

        print(f'[{num}]')
        print(f'브랜드 : {product_brand.text}')
        print(f'제품명 : {product_name_hood.text}')
        print(f'가 격 : {product_price.text}')
        print()

        num += 1
# rank_num = 1
# for i in items: 
#     delivery_option = i.select_one(".tag.display_tag_item")
#     if '빠른배송' in delivery_option.text:
#         # print(f'[{rank_num}]')
#         print(i.text)
#     # rank_num +=1


driver.quit()
