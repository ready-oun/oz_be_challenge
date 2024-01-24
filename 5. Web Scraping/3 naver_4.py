import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
key_word = input("검색어를 입력해주세요 : ")
# 탐색을 원하는 Url
url = base_url + key_word
# 탐색을 원하는 사이트의 데이터 달라고 요청 
req = requests.get(url, headers=header_user) 

html = req.text 
soup = BeautifulSoup(html, "html.parser")

# print(soup)

# 가져오고 싶은 HTML class 를 복붙해와서 저장~! 
# VIEW 탭의 글제목과 작성자 클래스 가져오기 
# title_link _cross_trigger : 글 제목
# name : 작성자
# view_wrap : 글 박스 데이터 싹 다 

total_area = soup.select(".view_wrap")

# 에러 처리
if total_area: 
    areas = total_area 
else :
    print("클래스를 변경해 주세요.")

# for문과 zip : Title & name 을 한 쌍으로 묶어서 i에 
for i in areas:
    title = i.select_one(".title_link._cross_trigger") # 두 클래스 사이에 ._ 임.. 점 1개만 넣는 게 아니라 
    name = i.select_one(".name")
    print(title.text)
    print(name.text)
    print(title['href']) # href로 타이틀에 포함된 링크 추출
    print() 

