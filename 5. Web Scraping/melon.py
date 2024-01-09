import requests
from bs4 import BeautifulSoup

# Inspect - Network - index.htm Click and cmd+R - bottom: User-Agent 
header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# class는 점(.)으로 구분한다.
 
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

lst_all = lst50 + lst100

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a") # 줄바꿈 없애기 - select_one().a 해서 a태그 선택? 
    singer = i.select_one(".checkEllipsis a")
    album = i.select_one(".ellipsis.rank03 a")
    
    # print(f'제목: {title.text.strip()}') # strip()으로 span - a 태그의 중복을 제거할 수 있는 라이브러리 
    print(f'순위: {rank}')
    print(f'제목: {title.text}')
    print(f'가수: {singer.text}')
    print(f'앨범: {album.text}')
    print()