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
    song_num = "".join(song_num) # 들여쓰기 주의ㅣㅣㅣㅣㅋㅋ
    return song_num # return으로 뱉어줘야 함
    
    # print(song_num)
    # print(type(song_num))

# get_nums(song_num_text) # 매개변수 아무 거나 넣어도 상관없다.

# singer ID value >> href="javascript:melon.link.goAlbumDetail('11352904');"

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# # class는 점(.)으로 구분한다.
 
lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

lst_all = lst50 + lst100

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

