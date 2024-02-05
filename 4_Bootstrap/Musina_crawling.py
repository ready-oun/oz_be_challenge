from bs4 import BeautifulSoup
from selenium import webdriver

#셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

#크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
#자동으로 크롬 드라이브를 최신으로 유지해주는 패키지 
from webdriver_manager.chrome import ChromeDriverManager 
#클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
#키보드 입력
from selenium.webdriver.common.keys import Keys

import time 

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = 'https://www.musinsa.com/app/'
driver.get(url)
time.sleep(0.5)

# link_list = []
# for i in range(1, 4):
#     print("*" *10, f'현재 {i} 페이지를 수집 중입니다.', "*"*10)
#     url_loop = f'https://www.musinsa.com/app/news/lists?page={i}&s_type=&q=&brand=&year_date=2024&month_date=&day_date=&type=2&pop=N'
#     driver.get(url_loop) 
#     elements = browser.find_elements(By.CLASS_NAME, 'gd_name')
#     for element in elements:
#         link = element.get_attribute('href')
#         link_list.append(link)

#     time.sleep(3)

# print(link_list)


# placeholder click and search
driver.find_element(By.CSS_SELECTOR, ".sc-1ppcy5v-3.ljHcMG").click() #searchbox
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".sc-1ppcy5v-3.ljHcMG").send_keys("겨울 싱글 코트") #input
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, ".sc-1ppcy5v-3.ljHcMG").send_keys(Keys.ENTER) # enter
time.sleep(0.5)

btn_all= driver.find_elements(By.CSS_SELECTOR, ".btn-all.font-mss")
for i in btn_all:
    if "상품 전체보기" in i.text:
        i.click()
        break
btn_all 

for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select('.li.li_box')

num = 1
for i in items:
    product_name = i.select_one(".list_info")

    if "코트" in product_name.text:
        product_brand = i.select_one(".item_title")
        product_price = i.select_one(".price") #p 회원가
        product_gender = i.select_one("icon_group") 

        print(f'[{num}]')
        print(f'브랜드 : {product_brand.text}')
        print(f'제품명 : {product_name.text}')
        print(f'가 격 : {product_price.text}')
        print(f'성 별 : {product_gender.text}')
        print()

        num += 1


# 상품 상세페이지
# url_goods = 'https://www.musinsa.com/app/goods/3753418'
    # 상세 페이지 내 클래스명 
        #제품명: product-detail__sc-1klhlce-3 fjguJZ
        #브랜드: product-detail__sc-achptn-9 dWHdxq
        #품번: product-detail__sc-achptn-4 flVcwF
        #성별: product-detail__sc-achptn-4 flVcwF
        #가격: product-detail__sc-1p1ulhg-7 hSwsZE
        #카테고리: product-detail__sc-up77yl-1 hYzMBL








