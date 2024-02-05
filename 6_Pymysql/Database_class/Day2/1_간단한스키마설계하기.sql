-- Day 2. 실습 1 - 간단한 스키마 설계하기 
-- (1) user 테이블 만들기 
-- id: 자동으로 생성됩니다. (PK)
-- password: 4자리 랜덤
-- name: 한글3자리
-- gender: male, female 중 랜덤선택
-- email: 5자리영문@gmail.com
-- birthday: 6자리 숫자 랜덤하게
-- age: 2자리 숫자 랜덤
-- company: [samsung, lg, hyundai]

USE ozbeclass; 
CREATE TABLE user (
	id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(4),
    name VARCHAR(3),
    gender ENUM('male', 'female'),
    email VARCHAR(15),
    birthday CHAR(6),
    age TINYINT,
    company ENUM('samsung', 'lg', 'hyundai')
);

-- Day2. (2) board 테이블 만들기
-- id 
-- title 5char
-- content 10char
-- likes: 1~100 사이 숫자 
-- -- CHECK 제약 조건: CHECK 제약 조건은 특정 조건을 충족하는 데이터만을 허용하는 제약 조건입니다. 
-- ---- likes INT 열에는 CHECK 제약 조건이 설정되어 있습니다. 이 조건은 likes 값이 1부터 100 사이의 범위에 속하는지 확인합니다. 따라서 likes 열에는 1부터 100 사이의 값만 저장될 수 있습니다.
-- img: "c" // img 열은 값이 지정되지 않을 경우 기본적으로 'c'라는 값을 가집니다. 이는 img 열에 다른 값이 지정되지 않으면 'c'로 초기화됩니다.
-- created: 오늘 날짜
-- user_id (foreign_key)

CREATE TABLE board (
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(5),
    content VARCHAR(10), 
    likes INT CHECK (likes BETWEEN 1 AND 100),
    img CHAR(1) DEFAULT 'c',
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)       
);    
