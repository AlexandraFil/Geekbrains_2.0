-- 1. Проанализировать какие запросы могут выполняться наиболее часто в процессе работы приложения и добавить необходимые индексы.

# Поиск по имени и фамилии/ только по фамилии

CREATE INDEX users_first_name_last_name_idx ON users(first_name, last_name);
CREATE INDEX users_last_name_idx ON users(last_name);

# Поиск по названию файла и типу медиа 

CREATE INDEX media_filename_media_type_id_idx ON media(filename, media_type_id);
CREATE INDEX media_filename_idx ON media(filename);

# По городу

CREATE INDEX profiles_hometown_idx ON profiles(hometown);

# Поиск в постах и сообщениях по заголовку и времени создания

CREATE INDEX posts_created_at_idx ON posts(created_at);
CREATE INDEX posts_head_created_at_idx ON posts(head, created_at);

CREATE INDEX messages_created_at_idx ON messages(created_at);
CREATE INDEX messages_head_created_at_idx ON messages(head, created_at);

SHOW CREATE TABLE users;

-- 2. Задание на оконные функции
-- Построить запрос, который будет выводить следующие столбцы:
-- имя группы
-- среднее количество пользователей в группах
-- самый молодой пользователь в группе
-- самый пожилой пользователь в группе
-- общее количество пользователей в группе
-- всего пользователей в системе
-- отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100

SELECT * FROM communities;
SELECT * FROM communities_users;

SELECT COUNT(communities.id) FROM communities;

SELECT DISTINCT communities.name, -- имя группы
	COUNT(communities_users.user_id) OVER () / 
		(SELECT COUNT(communities.id) FROM communities)
			AS average_members, -- среднее количество пользователей в группах
	MAX(profiles.birthday) OVER w AS youngest_member,-- самый молодой пользователь в группе
	MIN(profiles.birthday) OVER w AS eldest_member, -- самый пожилой пользователь в группе
	COUNT(communities_users.user_id) OVER w AS count_members, -- общее количество пользователей в группе
	COUNT(profiles.user_id) OVER() AS total_users, -- всего пользователей в системе
	COUNT(communities_users.user_id) OVER w / COUNT(profiles.user_id) OVER() * 100 AS "%%" -- отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100
		FROM (communities
			JOIN communities_users 
				ON communities.id = communities_users.community_id
					JOIN profiles 
						ON communities_users.user_id = profiles.user_id)
                WINDOW w AS (PARTITION BY communities_users.community_id);
                

-- 3. (по желанию) Задание на денормализацию
-- Разобраться как построен и работает следующий запрос:
-- Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.

SELECT users.id,
	COUNT(DISTINCT messages.id) +
	COUNT(DISTINCT likes.id) +
	COUNT(DISTINCT media.id) AS activity
FROM users
	LEFT JOIN messages
		ON users.id = messages.from_user_id
	LEFT JOIN likes
		ON users.id = likes.user_id
	LEFT JOIN media
		ON users.id = media.user_id
GROUP BY users.id
ORDER BY activity
LIMIT 10;

-- Правильно-ли он построен?
-- Какие изменения, включая денормализацию, можно внести в структуру БД
-- чтобы существенно повысить скорость работы этого запроса?