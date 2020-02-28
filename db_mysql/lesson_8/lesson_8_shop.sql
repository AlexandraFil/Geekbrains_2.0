USE shop;

DESC users;
DESC orders;

-- CROSS JOIN
SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users 
		CROSS JOIN orders;
	
SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users 
		JOIN orders;
		
SELECT * FROM users;
SELECT * FROM orders;

SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users, orders;

SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users, orders
	WHERE users.id = orders.user_id;

SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users
		JOIN orders
	ON users.id = orders.user_id;

SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users
		INNER JOIN orders
	ON users.id = orders.user_id;

SELECT users.name, COUNT(orders.user_id) AS total_orders
	FROM users
		JOIN orders
	ON users.id = orders.user_id
	GROUP BY orders.user_id
	ORDER BY total_orders;

SELECT u.name, COUNT(o.user_id) AS total_orders
	FROM users u
		JOIN orders o
	ON u.id = o.user_id
	GROUP BY o.user_id
	ORDER BY total_orders;
	
SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users
		LEFT JOIN orders # LEFT OUTER JOIN
	ON users.id = orders.user_id;
	
SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM users
		LEFT JOIN orders 
	ON users.id = orders.user_id
	WHERE orders.id IS NULL;
	
SELECT users.id, users.name, users.birthday_at, orders.id, orders.user_id
	FROM orders
		RIGHT JOIN users 
	ON users.id = orders.user_id
	WHERE orders.id IS NULL;
	
SELECT *
	FROM users
		FULL JOIN orders;