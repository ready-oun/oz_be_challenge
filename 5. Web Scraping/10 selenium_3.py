# 셀레니움 방식으로 변경하기

from selenium import webdriver
from bs4 import BeautifulSoup
import time 

header_user = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
key_word = input("검색어를 입력해주세요 : ")
# 탐색을 원하는 Url
url = base_url + key_word

# 탐색을 원하는 사이트의 데이터 달라고 요청 
driver = webdriver.Chrome() # init 
driver.get(url) 
time.sleep(5)

# 스크롤 실행 코드 
# driver.execute_script("window.scrollTo(0, 10000)") #js에서 써본 window.scrollTo... 0부터 3000 기준으로 스크롤 자동으로 내리게 함 
# 위에걸로는 택도 없어서..
    # Range(5) 해도 ㅇㅋ
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") # document.body.scrollHeight -- document. 빼먹지 말자..
    time.sleep(0.05)
# 스크롤을 수동으로 해주지 않으면 안 되노 .....
# 그렇다면 for 문을 돌리자 ! 
# 위치가 문제였다 ? 
    # html에 저장하기 전에 데이터들을 스크롤해서 가져와서 소스를 쌓아서 html에 담아야 한다. 그래서 위치를 앞으로 옮김.
    
html = driver.page_source #page source만 추출 
soup = BeautifulSoup(html, "html.parser") # html 구조화 

total_area = soup.select(".view_wrap")
ad_area = soup.select(".bx_type_ad")

# 에러 처리
if total_area: 
    areas = total_area 
else :
    print("클래스를 변경해 주세요.")



# for문과 zip : Title & name 을 한 쌍으로 묶어서 i에 
rank_num = 1 # 1. 넘버링 선언 
for i in areas:
    ad = i.select_one(".link_ad")
    if ad:
        # print(">광고주의<") 광고 빼고 순수 데이터만 추출하려면 continue로 직행 
        continue
    print(f'[{rank_num}]') # 3. 넘버링 출력 
    
    title = i.select_one(".title_link._cross_trigger") # 두 클래스 사이에 ._ 임.. 점 1개만 넣는 게 아니라 
    name = i.select_one(".name")
    print(title.text)
    print(name.text)
    print(title['href']) # href로 타이틀에 포함된 링크 추출
    print() 

    rank_num +=1 # 2. 넘버링 1씩 증가 
