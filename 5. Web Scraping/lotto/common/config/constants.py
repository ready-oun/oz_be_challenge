EMPTY_LINE = "-" * 20
LOTTO_MENU = "1) 당첨번호 보기\n" "2) 구매번호 생성하기\n" "3) 당첨내역 확인하기\n" "4) 종료\n\n" "입력 : "


READ_DATE = "조회 날짜 입력(2023-01-01): "
READ_ROUND = "조회 회차 입력(1101): "
READ_COUNT = "생성할 번호의 개수 입력: "

MINIMUM_INPUT_VALUE = 1
MAXIMUM_INPUT_VALUE = 4

WIN_NUMBER_DIRECTORY = "/data/winning"
USER_NUMBER_DIRECTORY = "/data/user"

WIN_NUMBER_FILE_PATTERN = WIN_NUMBER_DIRECTORY + "/%s.dat"
USER_NUMBER_FILE_PATTERN = USER_NUMBER_DIRECTORY + "/%s.dat"

PRINT_DRAW_ROUND_PATTERN = "\n당첨회차: %s"
PRINT_DRAW_NUMBER_PATTERN = "당첨번호: %s (보너스번호 : %s)\n"
PRINT_USER_NUMBER_PATTERN = "\n== %s회 생성내역 =="
PRINT_RANK_TITLE_PATTERN = "\n== %s회 당첨내역 =="
PRINT_RANK_DETAIL_PATTERN = "1등) %s개\n" "2등) %s개\n" "3등) %s개\n" "4등) %s개\n" "5등) %s개\n"

SHOW_WIN_NUMBERS = 1
GENERATE_NUMBERS = 2
CHECK_WIN_NUMBERS = 3
EXIT = 4

LOTTO_URL = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=%d"
NOT_WIN_RANK = -1

NUMBER_FORMAT_ERROR = "숫자를 입력하세요."
NUMBER_RANGE_ERROR = f"{MINIMUM_INPUT_VALUE} ~ {MAXIMUM_INPUT_VALUE}의 값을 입력할 수 있습니다."
DRAW_NUMBER_COUNT_ERROR = "추첨번호는 보너스 번호 포함 7개여야 합니다."
DATE_FORMAT_ERROR = "(2023-01-01) 형태의 데이터를 입력해야 합니다."
