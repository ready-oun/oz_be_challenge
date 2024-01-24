USE classicmodels;
-- -- -- <<기본 조회 및 필터링 >>
-- -- 고객 목록 조회: 모든 고객의 이름과 이메일을 조회하세요. TABLE: customers
-- SELECT customerName FROM customers;

-- -- 특정 제품 라인의 제품 조회: 'Classic Cars' 제품 라인에 속하는 모든 제품의 이름과 가격을 조회하세요. TABLE: products, COL: productLine
-- SELECT * FROM products WHERE productline = "Classic Cars";

-- -- 최근 주문: 가장 최근에 주문된 10개의 주문을 주문 날짜(orderDate)와 함께 조회하세요. TABLE: orders, COL: orderDate
-- SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

-- -- 최소 금액 이상의 결제: 100달러 이상 결제된 거래(amount)만 조회하세요. TABLE: payments, COL: amount 
-- SELECT * FROM payments WHERE amount >= 100;

-- -- << 조인 쿼리 >> 
-- -- 주문과 고객 정보 조합: 각 주문에 대한 주문 번호(orders-orderNumber)와 주문한 고객(customers-customerName)의 이름을 조회하세요.
-- SELECT o.orderNumber, c.customerName
-- FROM orders o
-- JOIN customers c ON o.customerNumber = c.customerNumber;

-- -- 제품과 제품 라인 결합: 각 제품의 이름(products-productName)과 속한 제품 라인의 설명(productlines-textDescription)을 조회하세요.
-- SELECT p.productName, p.productLine, pl.textDescription
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;

-- -- products와 productlines 전체 조회 
-- SELECT p.*, pl.*
-- FROM products p
-- JOIN productlines pl ON p.productLine = pl.productLine;

-- -- 직원과 상사 정보: 각 직원의 이름과 직속 상사의 이름을 조회하세요.
-- SELECT e1.employeeNumber, e1.firstName, e1.lastName, e2.firstName AS 'ManagerFirstName', e2.lastName AS 'ManagerLastName'
-- FROM employees e1
-- LEFT JOIN employees e2 ON e1.reportsTo = e2.employeeNumber;
-- --> Diane Murphy가 President라서 직속상사가 NULL인데도 출력되는 이유: LEFT JOIN으로 왼쪽employees테이블을 기준으로 조인하기 때문; 
-- --> LEFT JOIN을 사용하여 직원과 상사를 조인하는 쿼리를 실행하면, 상사가 있는 직원과 상사 정보가 함께 출력되지만, 상사가 없는 직원의 경우 상사 정보는 NULL로 표시.
-- --> employees 테이블은 같은 테이블을 나타내지만, e1과 e2로 나누는 이유는 조인 시에 같은 테이블을 참조할 때 구분하기 위한 별칭(alias)

-- -- 특정 사무실의 직원 목록: 'San Francisco' 사무실에서 근무하는 모든 직원의 이름을 조회하세요.
-- SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e.jobTitle
-- FROM employees e
-- JOIN offices o ON e.officeCode = o.officeCode
-- WHERE o.city = 'San Francisco';

-- -- << 그룹쿼리 >>
-- -- 제품 라인별 제품 수: 각 제품 라인에 속한 제품의 수를 조회하세요.
-- SELECT productLine, COUNT(*) AS productCount
-- FROM products
-- GROUP BY productLine; 

-- -- 고객별 총 주문 금액: 각 고객별로 총 주문 금액을 계산하세요.
-- SELECT customers.customerNumber,
-- 		customers.customerName,
--         SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
-- FROM customers
-- JOIN orders ON customers.customerNumber = orders.customerNumber
-- JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
-- GROUP BY customers.customerNumber, customers.customerName
-- ORDER BY totalAmount DESC;

-- -- 가장 많이 팔린 제품: 가장 많이 판매된 제품의 이름과 판매 수량을 조회하세요.
-- SELECT productName, SUM(quantityOrdered) AS totalQuantity
-- FROM orderdetails od
-- JOIN products p ON od.productCode = p.productCode
-- GROUP BY productName
-- ORDER BY totalQuantity DESC 
-- LIMIT 10;

-- -- 매출이 가장 높은 사무실: 가장 많은 매출을 기록한 사무실의 위치와 매출액을 조회하세요.
-- SELECT o.city, SUM(od. quantityOrdered * od.priceEach) AS totalSales
-- FROM orders ord
-- JOIN orderdetails od ON ord.orderNumber = od.orderNumber
-- JOIN customers c ON ord.customerNumber = c.customerNumber
-- JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
-- JOIN offices o ON e.officeCode = o.officeCode
-- GROUP BY o.city
-- ORDER BY totalSales DESC 
-- LIMIT 1;

-- -- << 서브쿼리 >> 
-- 특정 금액 이상의 주문: 500달러 이상의 총 주문 금액을 기록한 주문들을 조회하세요.
-- SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
-- FROM orderdetails
-- GROUP BY orderNumber
-- HAVING totalAmount > 500
-- ORDER BY totalAMount DESC;

-- -- 평균 이상 결제 고객: 평균 결제 금액보다 많은 금액을 결제한 고객들의 목록을 조회하세요.
-- SELECT customerNumber, SUM(amount) AS totalPayment
-- FROM payments
-- GROUP BY customerNumber
-- HAVING totalPayment > (SELECT AVG(amount) FROM payments)
-- ORDER BY totalPayment DESC;

-- -- 주문 없는 고객: 아직 주문을 하지 않은 고객의 목록을 조회하세요.
-- SELECT customerName
-- FROM customers
-- WHERE customerNumber NOT IN (SELECT customerNumber FROM orders)
-- ORDER BY customerName;

-- -- 최대 매출 고객: 가장 많은 금액을 지불한 고객의 이름과 총 결제 금액을 조회하세요.
-- SELECT c.customerName, SUM(od.quantityOrdered * od.priceEach) AS totalSpent
-- FROM customers c
-- JOIN orders o ON c.customerNumber = o.customerNumber
-- JOIN orderdetails od ON o.orderNumber = od.orderNumber
-- GROUP BY c.customerName
-- ORDER BY totalSpent DESC
-- LIMIT 1;

-- -- << ### **데이터 수정 및 관리**>>
-- -- 신규 고객 추가: 'customers' 테이블에 새로운 고객을 추가하는 쿼리를 작성하세요.
-- -- 현재 customerNumber가 없어서 실행이 안 됨. 
-- INSERT INTO customers (customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) 
-- VALUES ('New Customer', 'Lastname', 'Firstname', '123-456-7890', '123 Street', 'Suite 1', 'City', 'State', 'PostalCode', 'Country', 1002, 50000.00); 

-- -- 제품 가격 변경: 'Classic Cars' 제품 라인의 모든 제품 가격을 10% 인상하는 쿼리를 작성하세요.
-- UPDATE products
-- SET buyPrice = buyPrice * 1.10
-- WHERE productLine = 'Classic Cars';
-- --> 경고 메시지는 'buyPrice' 열의 데이터가 잘리는(truncated) 경고입니다. 이는 증가된 가격이 데이터베이스의 열 크기보다 크기 때문에 발생하는 경고입니다. 그러나 데이터가 잘리더라도 변경 작업은 성공적으로 수행되었습니다.
-- --> 제품의 가격을 변경할 때 데이터가 잘리지 않도록 열의 크기를 적절히 조정하거나, 데이터 타입을 변경하여 충분한 공간을 확보할 수 있습니다. 또는 가격 열의 소수점 자리수를 조정하여 데이터 손실 없이 가격을 증가시킬 수도 있습니다.

-- -- 고객 데이터 업데이트: 특정 고객의 이메일 주소를 변경하는 쿼리를 작성하세요.
-- UPDATE customers
-- SET phone = '010-0000-0000'
-- WHERE customerNumber = 103;

-- 직원 전보: 특정 직원을 다른 사무실로 이동시키는 쿼리를 작성하세요.
-- UPDATE employees
-- SET officeCode = '2' -- > 문자열 데이터 타입 = VARCHAR
-- WHERE employeeNumber = 1002; -- > 숫자 데이터 타입 = int