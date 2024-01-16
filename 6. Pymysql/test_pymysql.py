import pymysql

# (1) db connection
connection = pymysql.connect(
    host = '127.0.0.1', # 'localhost' 해도 됨.
    user='root',
    password='robin_robin',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor 
    # DictCursor = Dictionary 형태로 DB를 Cursor(Return)해달라! 라는 뜻. 
)

cursor = connection.cursor()

sql = "SELECT * FROM customers"
cursor.execute(sql)

customers = cursor.fetchone() 
print("customers : ", customers)
print("customers : ", customers['customerNumber'])
print("customers : ", customers['customerName'])
print("customers : ", customers['country'])

# Cursor: pymysql 라이브러리를 통해 sql문을 호출하고, 결과 값을 담는 컨테이너 옵젝트.
#         서버와 디비가 상호작용할 때 커서부터 생성해야한다.
# 1. execute() - sql statement 를 실행시키기 위해 execute 함수 호출
# 2. fetchone() - 조회된 결과로부터 데이터 1개(하나의 row)를 반환
# 3. fetchall() - 모든 데이터를 한꺼번에 클라이언트로 가져올 때 사용
# 4. fetchmany(n) - n개의 데이터를 반환


 