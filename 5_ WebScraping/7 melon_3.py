import requests
from bs4 import BeautifulSoup

# Inspect - Network - index.htm Click and cmd+R - bottom: User-Agent 
header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# song_num_text = "javascript:melon.link.goAlbumDetail('11352904')"
# print(song_num_text) 

# 괄호 안 숫자만 뽑아내기 
def get_nums(song_num_text):
    song_num = [] # 문자열의 문자가 한 글자씩 순서를 가진다. 
    for num in song_num_text:
        if num.isdigit(): #.isdigit() method로 ,, 10진수로 변환이 가능하면 10진수로 변환했을 때 나오는 숫자 반환, 숫자로 변형이 안 되면 0을 내보낸다. 0이란? False 라는 뜻.. (True는 1)
            song_num.append(num)
    song_num = "".join([num for num in song_num_text if num.isdigit()]) 
    return song_num # return으로 뱉어줘야 함
    
    # .join() 메서드는 문자열을 결합하는 데 사용하는 파이썬 내장 메서드. 문자열 결합 시, 리스트나 튜플과 같은 반복 가능한(iterable) 객체의 요소들을 하나의 문자열로 연결하는 데에도 사용
    # .join() 메서드는 문자열을 기준으로 요소들을 결합함. 호출한 문자열을 구분자로 사용, 구분자로 사용된 문자열 사이에 연결할 요소들 삽입. 
    # .isdigit() 메서드는 숫자만 추출

# get_nums(song_num_text) # 매개변수 아무 거나 넣어도 상관없다.

# singer ID value >> href="javascript:melon.link.goAlbumDetail('11352904');"

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# # class는 점(.)으로 구분한다.
 
# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")

# lst_all = lst50 + lst100

# < .find_all(class_ =[ , , , ...]) >
# lst_all = soup.find_all(class_= ["list50", "lst100"]) # class 뒤에 언더바(_)로 구분, .없이 클래스명만. // [] 안에 몇 개든 ㅇㅋ 

# < .select(". , . , .")
lst_all = soup.select(".lst50, .lst100") # select는 클래스인지 모르니까 클래스 명 앞에 .을 붙여야함. 

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a") # 줄바꿈 없애기 - select_one().a 해서 a태그 선택? 
    singer = i.select_one(".ellipsis.rank02 a") # 위치가 달라져서 오류가 난다 ? 
    singer_link = get_nums(singer["href"])

    album = i.select_one(".ellipsis.rank03 a")
    album_link = get_nums(album["href"])

    # print(f'제목: {title.text.strip()}') # strip()으로 span - a 태그의 중복을 제거할 수 있는 라이브러리 
    print(f'순위: {rank}')
    print(f'제목: {title.text}')
    print(f'가수: {singer.text} => 링크: https://www.melon.com/artist/timeline.htm?artistId={singer_link}')
    print(f'앨범: {album.text} => 링크: https://www.melon.com/album/detail.htm?albumId={album_link}')
    print()

# daum.net도 추천
# SSG.com 카테고리 들어가면 할 게 많다 ^-^ 
# 뭘 해야 할 지 모르겠다? 간이기획서를 먼저 작성하고, 뭘 검색할지부터 정한다. 
# 모바일에서만 제공하는 플랫폼은 셀레니움으로 모바일환경으로 접속해서 크롤링 가능함.
