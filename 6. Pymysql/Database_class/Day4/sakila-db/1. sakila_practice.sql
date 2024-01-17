USE sakila;
-- -- 1. 문제: 배우 'GUINESS PENELOPE'가 출연한 모든 영화의 제목을 조회하시오.
-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';z

-- -- 2. 문제: 각 카테고리별로 몇 개의 영화가 있는지 조회하시오.
-- SELECT c.name, COUNT(fc.film_id) as number_of_films
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- GROUP BY c.name;

-- -- 3. 문제: 고객 ID가 5인 고객의 모든 대여 기록을 조회하시오.
-- SELECT r.rental_date, f.title
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.fild_id
-- WHERE r.customer_id = 5;

-- -- 4. 문제: 가장 최근에 데이터베이스에 추가된 10개의 영화 제목을 조회하시오.
-- SELECT title
-- FROM film
-- ORDER BY release_year DESC, title
-- LIMIT 10;

-- ACADEMY DINOSAUR' 영화에 출연한 모든 배우의 이름을 조회하시오.
-- SELECT a.first_name, a.last_name
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- JOIN film f ON fa.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- -- 문제: 'ACADEMY DINOSAUR' 영화를 대여한 모든 고객의 이름을 조회하시오.
-- SELECT DISTINCT c.first_name, c.last_name
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- 문제: >각 고객별로< 가장 최근에 대여한 영화의 제목을 조회하시오.
-- SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- GROUP BY c.customer_id, c.first_name, c.last_name, f.title;

-- 문제: 각 영화별 >평균 대여 기간<을 일 단위로 계산하시오.: DATEDIFF( , )
-- AVG(return_date - rental_date)
-- SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title;

-- 문제: 가장 많이 대여된 영화의 제목과 대여 횟수를 조회하시오. : COUNT()
-- SELECT f.title, COUNT(r.rental_id) as rental_count
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- **문제**: 각 카테고리별 평균 대여 요금을 계산하시오. : AVG(f.rental_rate)
-- SELECT c.name, AVG(f.rental_rate) as avg_rental_rate
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- GROUP BY c.name;


-- ** 문제: 각 월별로 총 매출액을 계산하시오. : SUM(payment.amount) // YEAR MONTH **
-- SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales
-- FROM payment p
-- GROUP BY YEAR(p.payment_datE), MONTH(p.payment_date);

-- 문제: 각 배우별로 출연한 영화 수를 계산하시오.
-- SELECT a.first_name, a.last_name, COUNT(fa.film_id) as number_of_films
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- GROUP BY a.first_name, a.last_name;

-- 문제: 가장 많은 수익을 낸 영화의 제목과 수익을 조회하시오.

-- SELECT f.title, SUM(p.amount) AS total_revenue
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- GROUP BY f.title
-- ORDER BY total_revenue DESC
-- LIMIT 1;

-- 문제: 평균 대여 요금보다 높은 요금의 영화 제목과 요금을 조회하시오.
-- SELECT f.title, f.rental_rate
-- from film f
-- WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);

-- **문제**: 가장 많은 영화를 대여한 고객의 이름과 대여 횟수를 조회하시오.
-- SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rental_count
-- FROM rental r 
-- JOIN customer c ON r.customer_id = c.customer_id
-- GROUP BY c.customer_id
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- 문제: 배우 'PENELOPE GUINESS'가 출연한 영화 중 가장 많이 대여된 영화의 제목과 대여 횟수를 조회하시오. : AND
-- SELECT f.title, COUNT(r.rental_id) AS rental_count 
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
-- GROUP BY f.title
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- --
-- 문제: 'film' 테이블에 'New Adventure Movie'라는 새로운 영화를 추가하시오.
-- INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
-- VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown', 2023, 1, 3, 4.99, 120, 19.99, 'PG', 'Trailers,Commentaries');



-- **문제**: 고객 ID가 5인 고객의 주소를 '123 New Address, New City'로 변경하시오.
-- UPDATE customer
-- SET address_id = (SELECT address_id FROM address WHERE address = '123 New Address, New City')
-- WHERE customer_id = 5;


-- 문제: 대여 ID가 200인 대여 기록의 상태를 'returned'로 변경하시오.
-- UPDATE rental
-- SET return_date = NOW()
-- WHERE rental_id = 200;

-- 문제: 배우 ID가 10인 배우의 정보를 삭제하시오.
-- DELETE FROM actor
-- WHERE actor_id = 10;