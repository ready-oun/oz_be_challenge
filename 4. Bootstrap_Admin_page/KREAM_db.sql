USE KREAM;
-- CREATE TABLE category (
-- 	category_id INT PRIMARY KEY, 
--     category_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE product (
-- 	product_id INT PRIMARY KEY,
--     category_id INT, 
--     gender VARCHAR(10),
--     brand VARCHAR(255),
--     product_name VARCHAR(255),
--     price DECIMAL(10, 2) NOT NULL,
--     FOREIGN KEY (category_id) REFERENCES category(category_id)
-- );




-- category 
-- INSERT INTO category (category_id, category_name)
-- VALUES
-- 	(63, '아우터'),
--     (34, '신발'),
--     (64, '상의'),
--     (65, '하의'),
--     (9, '가방'),
--     (66, '지갑'),
--     (54, '시계'),
--     (7, '패션잡화'),
--     (67, '컬렉터블'),
--     (46, '뷰티'),
--     (11, '테크'),
--     (43, '캠핑'),
--     (68, '가구/리빙');

-- SELECT p.*, c.category_name
-- FROM product p
-- JOIN category c ON p.category_id = c.category_id;


update product p
join category c on p.category_name = c.category_name
SET p.category_id = c.category_id;