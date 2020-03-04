-- 2. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

SELECT * FROM likes;

SELECT profiles.user_id, profiles.birthday 
	FROM profiles
	ORDER BY birthday DESC
	LIMIT 10;

SELECT users.id, COUNT(*) AS likes_per_user
	FROM users
		JOIN profiles
			ON users.id = profiles.user_id
		LEFT JOIN likes 
			ON users.id = likes.target_id 
		LEFT JOIN target_types 
			ON likes.target_type_id = target_types.id 
	WHERE target_types.name = 'users' 
		AND users.id IN (SELECT * FROM(
			SELECT user_id FROM profiles ORDER BY birthday DESC LIMIT 10) AS sorted_profiles)
	GROUP BY users.id
	WITH ROLLUP;


-- 3. Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT sex, COUNT(*) AS total_likes
	FROM users
		JOIN profiles 
			ON users.id = profiles.user_id
		JOIN likes
			ON users.id = likes.user_id 
	GROUP BY sex 
	ORDER BY total_likes DESC; 


-- 4. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.

# Активность пользователей будем считать по количеству дейстий: 
# 1. отправленные этим пользователем сообщения (from_user_id в messages)
# 2. исходящие заявки в друзья (user_id в friendship)
# 3. поcтавленные лайки
# 4. посты пользователя

SELECT users.id, 
	CONCAT(first_name, ' ', last_name) AS user, 
	COUNT(DISTINCT(messages.created_at)) AS messages_activity, 
	COUNT(DISTINCT(likes.created_at)) AS likes_activity,
	COUNT(DISTINCT(media.created_at)) AS media_activity,
	(COUNT(DISTINCT(messages.created_at)) + COUNT(DISTINCT(likes.created_at)) + COUNT(DISTINCT(media.created_at))) AS overall_activity 
	FROM users
		JOIN profiles 
			ON users.id = profiles.user_id
		LEFT JOIN messages 
			ON users.id = messages.from_user_id 
		LEFT JOIN likes 
			ON users.id = likes.user_id
		LEFT JOIN media
			ON users.id = media.user_id
	GROUP BY users.id
	ORDER BY overall_activity
	LIMIT 10;

				
