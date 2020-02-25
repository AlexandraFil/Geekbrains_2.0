-- 1. Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять).


-- 2. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

SELECT * FROM target_types;

UPDATE likes 
	SET target_id = FLOOR(1 +(RAND() * 100))
		WHERE target_type_id = 2; #  пришлось чуть подправить данные
	
CREATE TEMPORARY TABLE youngest(
	SELECT user_id,
		TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age	
	FROM profiles
	ORDER BY age LIMIT 10);

SELECT * FROM youngest;
 
SELECT target_id, 
	COUNT(target_id)
FROM likes
	WHERE target_type_id IN(
		SELECT id 
			FROM target_types
				WHERE name = 'users')
	AND target_id IN(SELECT user_id FROM youngest)
GROUP BY target_id #  сколько каждый из самых молодых получил лайков
WITH ROLLUP; #  сколько суммарно

-- -- -- --

SELECT * FROM target_types;

SELECT * FROM profiles ORDER BY birthday DESC LIMIT 10;

SELECT * FROM likes WHERE target_type_id = 2;

SELECT target_id, COUNT(*) FROM likes
	WHERE target_type_id = 2
		AND target_id IN (SELECT * FROM(
			SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10
		) AS sorted_profiles)
		GROUP BY target_id;
	
SELECT SUM(likes_per_user) AS likes_total FROM(
	SELECT COUNT(*) AS likes_per_user
		FROM likes
			WHERE target_type_id = 2
				AND target_id IN(
					SELECT * FROM(
						SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10
					) AS sorted_profiles
				)
			GROUP BY target_id
) AS counted_likes;

-- 3. Определить кто больше поставил лайков (всего) - мужчины или женщины?

DESC profiles;
DESC likes;

-- Количество мужчин и женщин в моей базе
SELECT 
	COUNT(*) AS total,
	sex 
FROM 
	profiles
GROUP BY
	sex; # меня 38 f, 62 m

-- Количество мужчин и женщин поставивших лайки в моей базе
SELECT 
	(SELECT COUNT(user_id)
		FROM  likes WHERE user_id IN(
			SELECT user_id FROM profiles
				WHERE sex = 'm')) AS men,		# men - 160
	(SELECT COUNT(user_id) 
		FROM  likes WHERE user_id IN(
			SELECT user_id FROM profiles
				WHERE sex = 'f')) AS women;     # women - 90
			
-- Больше лайков поставили мужчины, но их больше в базе данных
-- Поэтому подсчитала сколько в среднем поставили лайков мужчины и женщины - мужчины чуть больше
SELECT 
	((SELECT COUNT(user_id)
		FROM  likes WHERE user_id IN(
			SELECT user_id FROM profiles
				WHERE sex = 'm')) / 
				(SELECT COUNT(user_id) 
					FROM profiles 
						WHERE sex = 'm')) AS men,		# men - 2,5806
	((SELECT COUNT(user_id)
		FROM  likes WHERE user_id IN(
			SELECT user_id FROM profiles
				WHERE sex = 'f')) / 
				(SELECT COUNT(user_id) 
					FROM profiles 
						WHERE sex = 'f')) AS women;		# women - 2,3684
						
-- -- -- --


						
						
-- 4. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.

# Активность пользователей будем считать по количеству дейстий: 
# 1. отправленные этим пользователем сообщения (from_user_id в messages)
# 2. исходящие заявки в друзья (user_id в friendship)
# 3. поcтавленные лайки
# 4. посты пользователя
						
SELECT * FROM posts;
SELECT * FROM messages;
SELECT * FROM friendship;
SELECT * FROM likes;

DROP table a;

CREATE TEMPORARY TABLE a (
	((SELECT user_id, 
		COUNT(user_id) AS actions 
	FROM posts 
	GROUP BY user_id)
		UNION
	(SELECT user_id, 
		COUNT(user_id) AS actions 
	FROM likes 
	GROUP BY user_id)
		UNION
	(SELECT user_id, 
		COUNT(user_id) AS actions 
	FROM friendship
	GROUP BY user_id)
		UNION
	(SELECT from_user_id AS user_id, 
		COUNT(from_user_id) AS actions 
	FROM messages
	GROUP BY user_id)));

SELECT * FROM a;

SELECT user_id, 
	SUM(actions) AS total_actions 
FROM a 
GROUP BY user_id 
ORDER BY total_actions LIMIT 10;
							
-- -- --

SELECT CONCAT(first_name, ' ', last_name) AS user,
	(SELECT COUNT(*) FROM likes WHERE likes.user_id = users.id) +
	(SELECT COUNT(*) FROM media WHERE media.user_id = users.id)
						
						
						
						
						
						
						
						
