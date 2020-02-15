-- Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”

-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	birthday_at DATE,
	created_at DATETIME,
	updated_at DATETIME
);

INSERT INTO 
	users (name, birthday_at, created_at, updated_at)
VALUES
	('Alex', '1983-07-26', NULL, NULL),
	('Max', '1985-07-13', NULL, NULL),
	('Maria', '1984-07-16', NULL, NULL),
	('Lucy', '1992-11-01', NULL, NULL),
	('Jane', '1985-12-12', NULL, NULL),
	('Ronald', '1986-03-29', NULL, NULL),
	('Michael', '1990-05-22', NULL, NULL),
	('Eddy', '1984-07-07', NULL, NULL);

UPDATE 
	users
SET
	created_at = NOW(),
	updated_at = NOW();

SELECT * FROM users;

-- 2. Таблица users была неудачно спроектирована. 
-- Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". 
-- Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	birthday_at DATE,
	created_at VARCHAR(255),
	updated_at VARCHAR(255)
);

INSERT INTO 
	users (name, birthday_at, created_at, updated_at)
VALUES
	('Alex', '1983-07-26', '20.10.2017 8:35', '20.10.2017 8:10'),
	('Max', '1985-07-13', '22.10.2018 14:10', '30.01.2020 18:10'),
	('Maria', '1984-07-16', '14.05.2017 13:00', '20.12.2019 12:05'),
	('Lucy', '1992-11-01', '10.01.2015 8:40', '09.03.2019 6:07'),
	('Jane', '1985-12-12', '29.12.2016 7:55', '20.01.2020 8:45'),
	('Ronald', '1986-03-29', '10.01.2013 9:20', '28.04.2017 8:10'),
	('Michael', '1990-05-22', '02.05.2010 8:10', '20.10.2011 10:15'),
	('Eddy', '1984-07-07', '01.01.2019 5:50', '01.01.2019 6:40');

UPDATE 
	users
SET
	created_at = STR_TO_DATE(created_at, '%d.%m.%Y %k:%i'),
	updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %k:%i');

ALTER TABLE
	users
CHANGE
	created_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE
	users
CHANGE
	updated_at updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

DESCRIBE users;

-- 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 
-- 0, если товар закончился и выше нуля, если на складе имеются запасы. 
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
-- Однако, нулевые запасы должны выводиться в конце, после всех записей.

CREATE TABLE storehouses_products (
	id SERIAL PRIMARY KEY,
	storehouse_id INT UNSIGNED,
	product_id INT UNSIGNED,
	value INT UNSIGNED,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO
	storehouses_products (storehouse_id, product_id, value)
VALUES
	(1, 23, 0),
	(2, 234, 12),
	(1, 24, 10),
	(1, 2, 0),
	(2, 3, 5),
	(1, 46, 36);

SELECT 
	storehouse_id, product_id, value 
FROM 
	storehouses_products
ORDER BY
	value = 0,
	value;

-- 4. (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
-- Месяцы заданы в виде списка английских названий ('may', 'august')

SELECT 
	name
FROM 
	users
WHERE 
	DATE_FORMAT(birthday_at, '%M') IN ('may', 'august');

-- 5. (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. 
-- SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.

CREATE TABLE catalogs (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) 
);

INSERT INTO catalogs VALUES
	(1, 'Процессоры'),
	(2, 'Материнские платы'),
	(3, 'Видеокарты'),
	(4, 'Жесткие диски'),
	(5, 'Оперативная память');

SELECT 
	*
FROM 
	catalogs 
WHERE 
	id IN (5, 1, 2)
ORDER BY 
	FIELD(id, 5, 1, 2);

-- Практическое задание теме “Агрегация данных”

-- 1. Подсчитайте средний возраст пользователей в таблице users

SELECT 
	AVG(TIMESTAMPDIFF(YEAR, birthday_at, NOW())) AS age
FROM 
	users;

-- 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
-- Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT 
	DATE_FORMAT(DATE(CONCAT_WS('-', YEAR(NOW()), MONTH(birthday_at), DAY(birthday_at))), '%W') AS day,
	COUNT(*) AS total
FROM 
	users
GROUP BY
	day
ORDER BY 
	total;

-- 3. (по желанию) Подсчитайте произведение чисел в столбце таблицы

SELECT 
	ROUND(EXP(SUM(LN(value)))) 
FROM
	storehouses_products;

