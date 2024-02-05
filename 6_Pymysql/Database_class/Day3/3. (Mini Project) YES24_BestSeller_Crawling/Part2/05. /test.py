from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pymysql
import re
from datetime import datetime

browser = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24'

link_list = []
for i in range(1, 4):
    print("*"*10, f'현재 {i} 페이지를 수집 중입니다.', "*"*10)
    browser.get(url)
    


