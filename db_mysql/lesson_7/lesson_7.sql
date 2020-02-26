-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

USE shop;
SHOW TABLES;
SELECT * FROM users;

INSERT INTO orders (user_id)
SELECT id FROM users WHERE name = 'Alex';

INSERT INTO orders_products (order_id, product_id, total)
SELECT LAST_INSERT_ID(), id, 2 FROM products 
WHERE name = 'Intel Core i5-7400';

INSERT INTO orders (user_id)
SELECT id FROM users WHERE name = 'Maria';

INSERT INTO orders_products (order_id, product_id, total)
SELECT LAST_INSERT_ID(), id, 1 FROM products 
WHERE name IN ('Intel Core i5-7400', 'Gigabyte H310M S2H');

INSERT INTO orders (user_id)
SELECT id FROM users WHERE name = 'Ronald';

INSERT INTO orders_products (order_id, product_id, total)
SELECT LAST_INSERT_ID(), id, 1 FROM products 
WHERE name IN ('AMD FX-8320', 'ASUS ROG MAXIMUS X HERO');

SELECT id, name, birthday_at FROM users;

SELECT 
	u.id, u.name, u.birthday_at
FROM 
	users AS u
JOIN
	orders AS O
ON 
	u.id = o.user_id;
	
-- Выведите список товаров products и разделов catalogs, который соответствует товару.

SELECT 
	p.id,
	p.name,
	p.price,
	c.name AS catalog
FROM
	products AS p
LEFT JOIN
	catalogs AS C
ON 
	p.catalog_id = c.id;
	
-- (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
-- Поля from, to и label содержат английские названия городов, поле name — русское. 
-- Выведите список рейсов flights с русскими названиями городов.

CREATE TABLE flights (
	id SERIAL PRIMARY KEY,
	`from` VARCHAR(255) COMMENT 'Город отправления',
	`to` VARCHAR(255) COMMENT 'Город прибытия'
) COMMENT = 'Рейсы';

INSERT INTO flights (`from`, `to`) VALUES
	('moscow', 'omsk'),
	('novgorod', 'kazan'),
	('irkutsk', 'moscow'),
	('omsk', 'irkutsk'),
	('moscow', 'kazan');

CREATE TABLE cities (
	id SERIAL PRIMARY KEY,
	label VARCHAR(255) COMMENT 'Код города',
	name VARCHAR(255) COMMENT 'Название города'
) COMMENT = 'Словарь городов';

INSERT INTO cities (label, name) VALUES
	('moscow', 'Москва'),
	('irkutsk', 'Иркутск'),
	('novgorod', 'Новгород'),
	('kazan', 'Казань'),
	('omsk', 'Омск');

SELECT 
	f.id,
	cities_from.name AS `from`,
	cities_to.name AS `to`
FROM flights AS f
	LEFT JOIN cities AS cities_from
		ON f.from = cities_from.label
	LEFT JOIN cities AS cities_to
		ON f.to = cities_to.label
ORDER BY id;
