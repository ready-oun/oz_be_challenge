# webdriver-manager 라이브러리 불러오기
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager().install()

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24'
browser.get(url)

# 1페이지 링크 데이터 전체 수집
### 1개 베스트셀러 링크 수집
browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('href')

### 1페이지 전체 링크 데이터
datas = browser.find_elements(By.CLASS_NAME, 'gd_name') # elements: LIST

for i in datas:
    print(i.get_attribute('href'))

# Page 3 까지 링크 데이터 전부 수집

import time
# from selenium import webdriver

# 브라우저 설정 및 초기화
# 예시: Chrome 브라우저 사용
browser = webdriver.Chrome()

url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24'

link_list = []
for i in range(1, 4):
    print("*" *10, f'현재 {i} 페이지를 수집 중입니다.', "*"*10)
    url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24'
    browser.get(url) 
    elements = browser.find_elements(By.CLASS_NAME, 'gd_name')
    for element in elements:
        link = element.get_attribute('href')
        link_list.append(link)

    time.sleep(3)

# print(link_list)

len(link_list)

# for link in link_list:
#     # 상세 페이지로 이동
#     browser.get(link)
browser.get(link_list[0]) # 여기서부터 에러가 났다. 

title = browser.find_element(By.CLASS_NAME, 'gd_name').text
author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
ranking = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(" | ")[1].split(" ")[1][:-1]
ranking_weeks = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(" | ")[1].split(" ")[2][:-1]

# 데이터베이스 연동 후 --> 수집한 데이터를 DB에 저장 (csv)
import pymysql # pip install pymysql
import time
import re
from datetime import datetime

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='robin_robin',
    db='yes24',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cur: 
    for i in link_list:
        browser.get(link)

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text

        match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)

        if match:
            year, month, day = match.groups()
            data_obj = datetime(int(year), int(month), int(day))
            publishing = data_obj.strftime("%Y-%-m-%d")
        else: 
            publishing = "2024-00-00"

        rating = browser.find_element(By.CLASS_NAME, 'yes_b').text
        
        review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
        review = int(review.replace(",", "")) # replace comma
        
        sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
        sales = int(sales.replace(",", ""))

        price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
        price = int(price.replace(",", ""))

        full_text = browser.find_element(By.CLASS_NAME, 'gd_best').text
        parts = full_text.split(" | ")

        if len(parts) == 1: # 빈칸 등으로 정상적으로 들어오지 않음
            ranking = 0
            ranking_weeks = 0 
        else:
            try:
                ranking_part = parts[0]
                ranking = ''.join(filter(str.isdigit, ranking_part)) # 문자데이터에서 숫자만 가져오기
            except:
                ranking = 0

            try:
                ranking_weeks_part = parts[1]
                ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))
            except:
                ranking_weeks = 0

        sql = """INSERT INTO Books(
            title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks
            )
            VALUES(
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
            """

        cur.execute(sql,(title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        conn.commit()

        time.sleep(2)