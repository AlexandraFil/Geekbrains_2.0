SELECT * FROM posts LIMIT 10;

DESC posts;

UPDATE posts SET media_id = NULL;

UPDATE posts SET media_id = (
	SELECT id FROM media WHERE media.user_id = posts.user_id LIMIT 1)
		WHERE  id IN (1, 15, 34, 56, 67, 8, 24, 89, 28, 55, 26);
		
SELECT * FROM posts WHERE media_id IS NOT NULL;

UPDATE profiles SET photo_id =
	(SELECT id FROM media 
		WHERE media.user_id = profiles.user_id 
			AND media.media_type_id = 1 LIMIT 1);
			
SELECT * FROM profiles LIMIT 20;

SELECT * FROM users LIMIT 20;

UPDATE users 
	SET phone = 
		(SELECT CONCAT_WS("-",
		FLOOR(100 + (RAND() * 899)),
		FLOOR(100 + (RAND() * 889)),
		FLOOR(10+ (RAND() * 89)),
		FLOOR(10+ (RAND() * 89)))
	);

DESC users;

ALTER TABLE users MODIFY phone VARCHAR(13);

DROP TABLE IF EXISTS likes;

CREATE TABLE likes (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	user_id INT UNSIGNED NOT NULL,
	target_id INT UNSIGNED NOT NULL,
	target_type_id INT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;
DROP TABLE events; # удалила таблицы, которые у меня были для лайков
DROP TABLE event_types;
DROP TABLE review_statuses;

DROP TABLE IF EXISTS target_types;
CREATE TABLE target_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO target_types (name) VALUES
	('messages'),
	('users'),
	('media'),
	('posts');

INSERT INTO likes 
	SELECT
		id,
		FLOOR(1 +(RAND() * 100)),
 		FLOOR(1 +(RAND() * 250)),
		FLOOR(1 +(RAND() * 4)),
		CURRENT_TIMESTAMP
	FROM messages;

SELECT * FROM likes LIMIT 10;

SELECT * FROM users WHERE id = 3;

SELECT 
	first_name, 
	last_name, 
	(SELECT filename FROM media WHERE id =
		(SELECT photo_id FROM profiles WHERE user_id = users.id LIMIT 1)) AS photo, 
	(SELECT hometown FROM profiles WHERE user_id = users.id) AS city
FROM users WHERE id = 5;

SELECT filename FROM media
	WHERE user_id = 5
		AND media_type_id =(
			SELECT id FROM media_types WHERE name = 'photo'
		);
	
SELECT CONCAT(
	'Пользователь ', 
	(SELECT CONCAT(first_name, ' ', last_name) 
		FROM users WHERE id = media.user_id),
	' добавил фото ',
	filename,
	' ',
	created_at) AS news
		FROM media
		WHERE user_id = 5
			AND media_type_id = (
				SELECT id FROM media_types WHERE name LIKE 'photo'
);

SELECT 
	(SELECT CONCAT(first_name, ' ', last_name) 
		FROM users WHERE id = media.user_id) AS owner,
	filename, 
	size
		FROM media
		ORDER BY size DESC 
		LIMIT 10;

DESC friendship;

	(SELECT friend_id FROM friendship WHERE user_id = 3)
UNION 
	(SELECT user_id FROM friendship WHERE friend_id = 3);

SELECT * FROM friendship_statuses;

(SELECT friend_id
	FROM friendship 
	WHERE user_id = 3
		AND status_id IN (
			SELECT id FROM friendship_statuses
				WHERE name = 'Confirmed'
		)
)
UNION 
(SELECT user_id
	FROM friendship 
	WHERE friend_id = 3
		AND status_id IN (
			SELECT id FROM friendship_statuses
				WHERE name = 'Confirmed'
		)
);

SELECT filename FROM media WHERE user_id IN (
	(SELECT friend_id
		FROM friendship 
		WHERE user_id = 3
			AND status_id IN (
				SELECT id FROM friendship_statuses
					WHERE name = 'Confirmed'
			)
	)
	UNION 
	(SELECT user_id
		FROM friendship 
		WHERE friend_id = 3
			AND status_id IN (
				SELECT id FROM friendship_statuses
					WHERE name = 'Confirmed'
			)
	)
);

SELECT filename, user_id, created_at FROM media WHERE user_id = 3
UNION 
SELECT filename, user_id, created_at FROM media WHERE user_id IN (
	(SELECT friend_id
		FROM friendship 
		WHERE user_id = 3
			AND status_id IN (
				SELECT id FROM friendship_statuses
					WHERE name = 'Confirmed'
			)
	)
	UNION 
	(SELECT user_id
		FROM friendship 
		WHERE friend_id = 3
			AND status_id IN (
				SELECT id FROM friendship_statuses
					WHERE name = 'Confirmed'
			)
	)
);

SELECT user_id, SUM(size) AS total
	FROM media
	GROUP BY user_id 
	HAVING total > 100000000
	ORDER BY total DESC;

SELECT target_id AS mediafile, COUNT(*) AS likes
	FROM likes 
		WHERE target_id IN (
			SELECT id FROM media WHERE user_id = 5
				UNION 
			(SELECT id FROM media WHERE user_id IN (
				SELECT friend_id
					FROM friendship
						WHERE user_id = 5
							AND status_id IN(
								SELECT id FROM friendship_statuses 
									WHERE name = 'Confirmed'
							)))
				UNION 
			(SELECT id FROM media WHERE user_id IN (
				SELECT user_id
					FROM friendship 
						WHERE friend_id = 5
							AND status_id IN (
								SELECT id FROM friendship_statuses
									WHERE name = 'Confirmed'
							)))
		)
		AND target_type_id = (SELECT id FROM target_types WHERE name = 'media')
		GROUP BY target_id;

SELECT COUNT(id) AS news, 
	MONTHNAME(created_at) AS month,
	MONTH(created_at) AS month_num
		FROM media 
			WHERE YEAR(created_at) = YEAR(NOW())
		GROUP BY month_num, month
		ORDER BY month_num DESC;

DESC messages;

SELECT from_user_id, to_user_id, body, is_delivered, created_at
	FROM messages 
		WHERE from_user_id = 3
			OR to_user_id = 3
		ORDER BY created_at DESC;
	
SELECT from_user_id, 
	to_user_id,
	head,
	body, 
	IF(is_delivered, 'delivered', 'not delivered') AS status 
		FROM messages
	    	WHERE (from_user_id = 3 OR to_user_id = 3)
	    ORDER BY created_at DESC;
    
SELECT 
	(SELECT CONCAT(first_name, ' ', last_name) 
    	FROM users 
        WHERE id = user_id) AS friend,           -- имя пользователя
    CASE (sex)                       
        WHEN 'm' THEN 'man'
        WHEN 'f' THEN 'woman'
    END AS sex,                                  -- пол
    TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age -- возраст
FROM profiles
	WHERE user_id IN (
		(SELECT friend_id
			FROM friendship 
			WHERE user_id = 3
				AND status_id IN (
					SELECT id FROM friendship_statuses
						WHERE name = 'Confirmed'
				)
		)
		UNION 
		(SELECT user_id
			FROM friendship 
			WHERE friend_id = 3
				AND status_id IN (
					SELECT id FROM friendship_statuses
						WHERE name = 'Confirmed'
				)
		));
    
-- Шаблоны имени  

SELECT CONCAT(first_name, ' ', last_name) AS fullname  
	FROM users
	WHERE last_name LIKE 'M%';
  
-- Регулярные выражения (на L не нашлось)

SELECT CONCAT(first_name, ' ', last_name) AS fullname  
	FROM users
	WHERE last_name RLIKE '^M.*z$';






















