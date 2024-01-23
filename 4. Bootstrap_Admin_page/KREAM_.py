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

#대기시간.. 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 
import pymysql

# sql conn
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'robin_robin',
    db='KREAM',
    charset='utf8mb4'
)

connection.cursor()

try:
    with connection.cursor() as cursor:

        user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

        options_ = Options()
        options_.add_argument(f"User-Agent={user}")
        options_.add_experimental_option("detach", True)
        options_.add_experimental_option("excludeSwitches", ["enable-logging"])

        #크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options_)
        wait = WebDriverWait(driver, 10)
        # 대기시간..

        url = 'https://kream.co.kr/search'
        driver.get(url)
        time.sleep(0.5)

        categories = {
            63: '아우터',
            34: '신발',
            64: '상의',
            65: '하의',
            9: '가방',
            66: '지갑',
            54: '시계',
            7: '패션잡화',
            67: '컬렉터블',
            46: '뷰티',
            11: '테크',
            43: '캠핑',
            68: '가구/리빙'
        }

        gender = {
            '&gender=men' : '남성',
            '&gender=women' : '여성',
            '&gender=kids' : '키즈'
        }
        gender_keys = list(gender.keys())
        gender_name = list(gender.values())

        base_url = 'https://kream.co.kr/search?shop_category_id='
        cat_ids = list(categories.keys())
        cat_names = list(categories.values())

        for cat_id, cat_name in categories.items():
            cat_gen_url = ''
            if cat_id in [7, 67, 46, 11, 43, 68]:
                cat_gen_url = f'{base_url}{cat_id}'
                print("*" * 10, f"{cat_name}에서 상품 페이지를 읽고 있습니다.", "*" * 10)
                driver.get(cat_gen_url)
                time.sleep(0.5)

                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                items = soup.select('.item_inner')

                for i in items:
                    product_brand = i.select_one(".product_info_brand.brand")
                    product_name = i.select_one(".product_info_product_name")
                    product_price = i.select_one(".amount")

                    # Gender undef
                    gen_val = None
                    #insert into
                    q_insert = '''INSERT INTO product (
                    category_name, gender, brand, product_name, price
                    ) 
                    VALUES (%s, %s, %s, %s, %s)
                    '''
                    to_tuple = (cat_name, gen_val, product_brand.text, product_name.text, product_price.text)
                    cursor.execute(q_insert, to_tuple)                
            else:
                for gen_key, gen_name in gender.items():
                    cat_gen_url = f'{base_url}{cat_id}{gen_key}'
                    print("*" *10, f"{cat_name} - {gen_name}에서 상품 페이지를 읽고 있습니다.", "*" *10)
                    time.sleep(0.5)

                    driver.get(cat_gen_url)

                    html = driver.page_source
                    soup = BeautifulSoup(html, "html.parser")
                    items = soup.select('.item_inner')

                    for i in items:
                        product_brand = i.select_one(".product_info_brand.brand")
                        product_name = i.select_one(".product_info_product_name")
                        product_price = i.select_one(".amount")

                        # Gender undef
                        gen_val = gen_name
                        #insert into
                        q_insert = '''INSERT INTO product (
                        category_name, gender, brand, product_name, price
                        ) 
                        VALUES (%s, %s, %s, %s, %s)
                        '''
                        to_tuple = (cat_name, gen_val, product_brand.text, product_name.text, product_price.text)
                        cursor.execute(q_insert, to_tuple)

    connection.commit()

finally: 
    driver.quit()
    connection.close()
                           