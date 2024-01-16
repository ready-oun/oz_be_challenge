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
SELECT customers.customerNumber,
		customers.customerName,
        SUM(orderdetails.quantityOrdered * orderdetails.priceEach) AS totalAmount
FROM customers
-- JOIN orders ON customers.customerNumber = orders.customerNumber
-- JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
-- GROUP BY customers.customerNumber, customers.customerName;