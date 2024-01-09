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

title = soup.select(".title_link._cross_trigger") # 클래스가 두 개인데, 공백을 잘 못 봐서 . 두개로 구분
name = soup.select(".name")

# print(name)
# print(type(name)) # 형변환 된다잉 
# print(list(name)) # 출력되는 걸 하나씩 꺼내서 출력하도록 하기 위해 >반복작업<을 해결하는 for문을 이용하기 위해 형변환. 

# for문과 zip : Title & name 을 한 쌍으로 묶어서 i에 
for i in zip(title, name): 
    print("--------------------")
    print(i[0].text) #[슈퍼스타, 흥민짱] 0, 1 // 0만 출력
    print(i[1].text) # 1만 출력 // .text 를 통해 텍스트만 추출 
    print(i[0]["href"]) # href로 타이틀에 포함된 링크 추출
    print() 
    print("--------------------")
