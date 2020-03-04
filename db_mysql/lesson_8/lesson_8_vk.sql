USE vk;

SELECT first_name, last_name, email, sex, birthday, hometown
	FROM users
		INNER JOIN profiles 
			ON users.id = profiles.user_id 
	WHERE users.id = 3;
	
SELECT users.first_name, users.last_name, media.user_id, media.filename, media.created_at 
	FROM media 
		JOIN users 
			ON media.user_id = users.id 
	WHERE  media.user_id = 5;
	
DESC media;
SELECT * FROM media_types;

SELECT users.first_name, users.last_name, media.user_id, media.filename, media.created_at 
	FROM media 
		JOIN users 
			ON media.user_id = users.id 
		JOIN media_types 
			ON media.media_type_id = media_types.id 
	WHERE  media.user_id = 5 AND media_types.name = 'photo';
	
SELECT DISTINCT media.user_id, media.filename, media.created_at 
	FROM media
		JOIN friendship 
			ON media.user_id = friendship.user_id
				OR media.user_id = friendship.friend_id
		JOIN users 
			ON users.id = friendship.friend_id 
				OR users.id = friendship.user_id
	WHERE  users.id = 5 AND media.user_id != 5
	ORDER BY user_id;

DESC friendship;

SELECT user_id, friend_id FROM friendship WHERE user_id = 5 OR friend_id = 5;

SELECT DISTINCT media.user_id, media.filename, media.created_at 
	FROM media
		JOIN friendship 
			ON media.user_id = friendship.user_id
				OR media.user_id = friendship.friend_id
		JOIN media_types 
			ON media.media_type_id = media_types.id
		JOIN users 
			ON users.id = friendship.friend_id 
				OR users.id = friendship.user_id
	WHERE  users.id = 55 AND media_types.name = 'photo'
	ORDER BY user_id;

SELECT messages.head, messages.body, users.first_name, users.last_name, messages.created_at 
	FROM messages 
		JOIN users 
			ON users.id = messages.to_user_id 
	WHERE messages.from_user_id = 55;

SELECT head, body, first_name, last_name, messages.created_at 
	FROM messages 
		JOIN users 
			ON users.id = messages.from_user_id 
	WHERE messages.to_user_id = 55;

SELECT messages.from_user_id, messages.to_user_id, messages.head, messages.created_at 
	FROM users 
		JOIN messages
			ON users.id = messages.to_user_id 
				OR users.id = messages.from_user_id 
	WHERE users.id = 55;


SELECT users.id, first_name, last_name, COUNT(requested_at) AS total_friends
	FROM users 
		LEFT JOIN friendship 
	 		ON users.id = friendship.user_id 
	 			OR users.id = friendship.friend_id 
	GROUP BY  users.id
	ORDER BY total_friends DESC;

SELECT * FROM friendship WHERE  user_id = 43 OR friend_id = 43;

SELECT likes.target_id,
	media.filename,
	target_types.name AS target_type,
	COUNT(DISTINCT(likes.id)) AS total_likes,
	CONCAT(first_name, ' ', last_name) AS owner
	FROM media
		LEFT JOIN likes 
			ON media.id = likes.target_id 
		LEFT JOIN target_types 
			ON likes.target_type_id = target_types.id 
		LEFT JOIN users 
			ON users.id = media.user_id 
	WHERE users.id = 55 AND target_types.name = 'media'
	GROUP BY media.id;

SELECT users.id, first_name, last_name, COUNT(*) AS total_likes
	FROM users 
		JOIN media 
			ON users.id = media.user_id 
		JOIN likes 
			ON media.id = likes.target_id 
		JOIN target_types 
			ON likes.target_type_id = target_types.id 
	WHERE target_types.name = 'media'
	GROUP BY users.id 
	ORDER BY total_likes DESC 
	LIMIT 10;

SELECT * FROM media WHERE user_id = 27;
SELECT * FROM likes WHERE target_id IN (26, 73, 97) AND target_type_id = 3;

