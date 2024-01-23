from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# 크롤링한 데이터를 저장할 리스트
product_list = []

# 크롬 드라이버 설정
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
options_ = Options()
options_.add_argument(f"User-Agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)
wait = WebDriverWait(driver, 10)

# 크롤링할 사이트 URL
url = 'https://kream.co.kr/search'
driver.get(url)
time.sleep(0.5)

# 카테고리와 성별 정보 설정
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

base_url = 'https://kream.co.kr/search?shop_category_id='
cat_ids = list(categories.keys())
cat_names = list(categories.values())

# 각 카테고리 및 성별에 대해 크롤링
for cat_id, cat_name in categories.items():
    cat_gen_url = ''
    if cat_id in [7, 67, 46, 11, 43, 68]:
        cat_gen_url = f'{base_url}{cat_id}'
        driver.get(cat_gen_url)
        time.sleep(1)
        print(cat_gen_url)
        # print("*" * 10, f"{cat_name}에서 상품 페이지를 읽고 있습니다.", "*" * 10)
    else:
        for gen_key, gen_name in gender.items():
            cat_gen_url = f'{base_url}{cat_id}{gen_key}'
            # print(cat_gen_url)
            # print("*" * 10, f"{cat_name} - {gen_name}에서 상품 페이지를 읽고 있습니다.", "*" * 10)
            # time.sleep(0.5)
            print(cat_gen_url)
            driver.get(cat_gen_url)
            time.sleep(1)

            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            items = soup.select('.item_inner')

            for i in items:
                product_brand = i.select_one(".product_info_brand.brand")
                product_name = i.select_one(".product_info_product_name")
                product_price = i.select_one(".amount") 

                # 데이터를 리스트에 추가
                product_list.append([
                    cat_name,
                    gen_name,
                    product_brand.text,
                    product_name.text,
                    product_price.text
                ])

# 크롤링이 끝난 후 드라이버 종료
time.sleep(5)            
driver.quit()

# 크롤링한 데이터 출력
# for product in product_list:
#     gender = product[1]
#     if not gender:
#         gender = "미분류"
#     print(f'카테고리 : {product[0]}')
#     print(f'성 별 : {gender}')
#     print(f'브랜드 : {product[2]}')
#     print(f'제품명 : {product[3]}')
#     print(f'가 격 : {product[4]}')
#     print()
