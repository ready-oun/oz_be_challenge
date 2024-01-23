from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymysql

def initialize_driver():
    user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options_ = Options()
    options_.add_argument(f"User-Agent={user}")
    options_.add_experimental_option("detach", True)
    options_.add_experimental_option("excludeSwitches", ["enable-logging"])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options_)
    return driver

def insert_product(cursor, cat_name, gen_val, product_brand, product_name, product_price):
    q_insert = '''INSERT INTO product (
        category_name, gender, brand, product_name, price
    ) 
    VALUES (%s, %s, %s, %s, %s)
    '''
    to_tuple = (cat_name, gen_val, product_brand.text, product_name.text, product_price.text)
    cursor.execute(q_insert, to_tuple)

def scrape_products(driver, cat_gen_url, cat_name, gen_name, connection, cursor):
    driver.get(cat_gen_url)
    time.sleep(0.5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select('.item_inner')

    for i in items:
        product_brand = i.select_one(".product_info_brand.brand")
        product_name = i.select_one(".product_info_product_name")
        product_price = i.select_one(".amount")

        gen_val = gen_name if gen_name else None
        insert_product(cursor, cat_name, gen_val, product_brand, product_name, product_price)

def scrape_category(driver, base_url, cat_id, cat_name, gender, connection, cursor):
    cat_gen_url = ''

    if cat_id in [7, 67, 46, 11, 43, 68]:
        cat_gen_url = f'{base_url}{cat_id}'
        print("*" * 10, f"{cat_name}에서 상품 페이지를 읽고 있습니다.", "*" * 10)
        scrape_products(driver, cat_gen_url, cat_name, None, connection, cursor)
        time.sleep(0.5)
    else:
        for gen_key, gen_name in gender.items():
            cat_gen_url = f'{base_url}{cat_id}{gen_key}'
            print("*" * 10, f"{cat_name} - {gen_name}에서 상품 페이지를 읽고 있습니다.", "*" * 10)
            time.sleep(0.5)
            scrape_products(driver, cat_gen_url, cat_name, gen_name, connection, cursor)

def scrape_all_categories(driver, base_url, categories, gender, connection, cursor):
    for cat_id, cat_name in categories.items():
        scrape_category(driver, base_url, cat_id, cat_name, gender, connection, cursor)
        time.sleep(0.5)

def main():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='robin_robin',
            db='KREAM',
            charset='utf8mb4'
        )

        with connection.cursor() as cursor:
            driver = initialize_driver()

            url = 'https://kream.co.kr/search'
            driver.get(url)
            time.sleep(0.5)

            base_url = 'https://kream.co.kr/search?shop_category_id='

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
                '&gender=men': '남성',
                '&gender=women': '여성',
                '&gender=kids': '키즈'
            }

            scrape_all_categories(driver, base_url, categories, gender, connection, cursor)

        connection.commit()

    finally:
        driver.quit()
        connection.close()

if __name__ == "__main__":
    main()
