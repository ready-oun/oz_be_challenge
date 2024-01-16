import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='robin_robin',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # # 문제1: 새로운 제품 추가
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # connection.commit()

    # # 문제2: 고객 목록 조회
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall():
    #     print(book)

    # # 문제3: 제품 재고 업데이트
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql, (1, 1))
    # connection.commit()

    # # 문제4: 고객별(GROUP BY) 총 주문 금액 
    # sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # # 문제5: 고객 이메일 업데이트
    # sql = "UPDATE Customers SET email=%s WHERE customerID = %s"
    # cursor.execute(sql, ('update@example.com', 1))
    # connection.commit()

    # # 문제6: 주문 취소
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15))
    # connection.commit()

    # 문제7: 특정 제품 검색 
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"
    # cursor.execute(sql, ('%Book%')) # Book 앞뒤로 anything is OK
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data['productName']) # 지금은 DictCursor 형태라: data.productName 이 아닌 딕트 형태로.

    # 문제 8: 특정 고객의 주문 데이터 조회
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data)
    
    # 문제 9. 가장 많이 주문한 고객 (주문횟수가 가장 많은 고객을 뽑자)
    sql = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders GROUP BY customerID 
        ORDER BY orderCount DESC LIMIT 1
        """
    
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)

cursor.close()

#  - **(2) 실전 연습 문제**
#     1. **새로운 제품 추가**: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
#     2. **고객 목록 조회**: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
#     3. **제품 재고 업데이트**: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
#     4. **고객별 총 주문 금액 계산**: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
#     5. **고객 이메일 업데이트**: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
#     6. **주문 취소**: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
#     7. **특정 제품 검색**: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
#     8. **특정 고객의 모든 주문 조회**: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
#     9. **가장 많이 주문한 고객 찾기**: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.