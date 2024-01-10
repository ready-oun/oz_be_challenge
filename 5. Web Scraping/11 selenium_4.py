from selenium import webdriver

#selenium에 다양한 옵션을 적용시키기 위한 패키지 
from selenium.webdriver.chrome.options import Options

# Chrome Driver Manger를 실행하기 위해 설치해주는 패키지 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# 기본설정 1. 
# option 설정을 넣기 위한 초기화 
options = Options()

# 
options.add_argument(f'user-agent={user_agent}') # user-agent 소문자로 작성해야 인식함
options.add_experimental_option('detach', True) #options에 ~~옵션에 있는 detach를 실행 >사이트 닫히지 않도록<


# 기본설정 2. 
# 거슬리는 메시지(터미널)
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 

# 기본설정 3. 
# '자동화된 소프트웨어에 의해 제어되고 있습니다' 창?알러트? 거슬리는 메시지(웹) 안 보이게
options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 오 안 보인다.. 보일 수도 있고 안 보일 수도 있다더라 
# ㄴ
# 차단 회피 ; 셀레니움 디버그 모드로 실행하기 (나중에 구글링해보셈)

# # 음소거 옵션 추가 (영상 크롤링 같은 거 할 때)
# options.add_argument("--mute-audio") 

# # 시크릿모드로 접속 
# options.add_argument('incognito')

# 화면 없이 크롤링하기 
# options.add_argument("--headLess") # L 대문자여야 함!!!!! 

# 화면 크기 
# options.add_argument("--start-maximized") # add ~ 옵션이 다 다르다 : selenium 공식문서 참고 selenium.dev/documentation/ 에서 Browser Options 검색 
# options.add_argument("--start-fullscreen")
                                #    가로, 세로
# options.add_argument("--window-size=1000, 4500")

service = Service(ChromeDriverManager().install()) # install service or update to recent ver. automatically 
driver = webdriver.Chrome(service=service, options=options) # 기존 디폴트에서 괄호 안에 옵션을 넣는 겨 

url = "https://kream.co.kr" # 빈 창으로 뜬다면, URL 주소에 오타가 있을 거임 
driver.get(url)

