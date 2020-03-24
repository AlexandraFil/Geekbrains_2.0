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
               
-- -- --

SELECT DISTINCT 
  communities.name AS group_name,
  COUNT(communities_users.user_id) OVER() 
    / (SELECT COUNT(*) FROM communities) AS avg_users_in_groups,
  FIRST_VALUE(users.id) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate DESC) AS youngest,
  FIRST_VALUE(users.id) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate) AS oldest,
  COUNT(communities_users.user_id) 
    OVER(PARTITION BY communities.id) AS users_in_groups,
  COUNT(users.id) OVER() AS users_total,
  COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) 
    / COUNT(users.id) OVER() *100 AS '%%'
    FROM communities
      JOIN communities_users 
        ON communities_users.community_id = communities.id
      JOIN users 
        ON communities_users.user_id = users.id
      JOIN profiles 
        ON profiles.user_id = users.id;

-- Выводим имена пользователей        
SELECT DISTINCT 
  communities.name AS group_name,
  COUNT(communities_users.user_id) OVER() 
    / (SELECT COUNT(*) FROM communities) AS avg_users_in_groups,
  FIRST_VALUE(users.first_name) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate DESC) AS youngest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate DESC) AS youngest_last_name,
  FIRST_VALUE(users.first_name) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate) AS oldest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER(PARTITION BY communities.id ORDER BY profiles.birthdate) AS oldest_last_name,
  COUNT(communities_users.user_id) 
    OVER(PARTITION BY communities.id) AS users_in_groups,
  COUNT(users.id) OVER() AS users_total,
  COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) 
    / COUNT(users.id) OVER() *100 AS '%%'
    FROM communities
      JOIN communities_users 
        ON communities_users.community_id = communities.id
      JOIN users 
        ON communities_users.user_id = users.id
      JOIN profiles 
        ON profiles.user_id = users.id;        

-- Выносим определения некоторых окон
SELECT DISTINCT 
  communities.name AS group_name,
  COUNT(communities_users.user_id) OVER() 
    / (SELECT COUNT(*) FROM communities) AS avg_users_in_groups,
  FIRST_VALUE(users.first_name) 
    OVER birthday_desc AS youngest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER birthday_desc AS youngest_last_name,
  FIRST_VALUE(users.first_name) 
    OVER birthday_asc AS oldest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER birthday_asc AS oldest_last_name,
  COUNT(communities_users.user_id) 
    OVER(PARTITION BY communities.id) AS users_in_groups,
  COUNT(users.id) OVER() AS users_total,
  COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) 
    / COUNT(users.id) OVER() *100 AS '%%'
    FROM communities
      JOIN communities_users 
        ON communities_users.community_id = communities.id
      JOIN users 
        ON communities_users.user_id = users.id
      JOIN profiles 
        ON profiles.user_id = users.id
      WINDOW birthday_desc AS (PARTITION BY communities.id ORDER BY profiles.birthdate DESC),
             birthday_asc AS (PARTITION BY communities.id ORDER BY profiles.birthdate);

           
-- Доработка расчёта общего количества пользователей в системе
-- Применяем внешнее объединение так как иначе не будут выведены группы, у которых нет членов

SELECT DISTINCT 
  communities.name AS group_name,
  COUNT(communities_users.user_id) OVER() 
    / (SELECT COUNT(*) FROM communities) AS avg_users_in_groups,
  FIRST_VALUE(users.first_name) 
    OVER birthday_desc AS youngest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER birthday_desc AS youngest_last_name,
  FIRST_VALUE(users.first_name) 
    OVER birthday_asc AS oldest_first_name,
  FIRST_VALUE(users.last_name) 
    OVER birthday_asc AS oldest_last_name,
  COUNT(communities_users.user_id) 
    OVER(PARTITION BY communities.id) AS users_in_groups,
  (SELECT COUNT(*) FROM users) AS users_total,
  COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) 
    / (SELECT COUNT(*) FROM users) *100 AS '%%'
    FROM communities
      LEFT JOIN communities_users 
        ON communities_users.community_id = communities.id
      LEFT JOIN users 
        ON communities_users.user_id = users.id
      LEFT JOIN profiles 
        ON profiles.user_id = users.id
      WINDOW birthday_desc AS (PARTITION BY communities.id ORDER BY profiles.birthdate DESC),
             birthday_asc AS (PARTITION BY communities.id ORDER BY profiles.birthdate);  
                

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

-- Для ускорения этого запроса можно создать таблицу activities, куда складывать
-- по триггеру ссылку на созданные пользователем сообщения, поставленные лайки
-- и добавленные файлы
 
 DROP TABLE IF EXISTS activities;
 CREATE TABLE IF NOT EXISTS activities (
 	id int(10) unsigned NOT NULL AUTO_INCREMENT,	
	user_id int(10) unsigned NOT NULL,
	activity_type_id int(10) unsigned NOT NULL,
	activity_id int(10) unsigned NOT NULL,
	primary key (id),
	foreign key (user_id) references users(id),
	foreign key (activity_type_id) references target_types(id),
	index activities_user_id_idx (user_id)
 )
 
 insert into target_types (name) values ('likes');
 
 DELIMITER //
 CREATE TRIGGER add_messages_to_activities AFTER INSERT ON messages
 FOR EACH ROW 
 BEGIN
	 INSERT INTO activities (user_id, activity_type_id, activity_id) VALUES (
		NEW.from_user_id,
	 	(SELECT id FROM target_types tt where tt.name = 'messages'),
	 	NEW.id
	 );
 END //
 
 CREATE TRIGGER add_likes_to_activities AFTER INSERT ON messages
 FOR EACH ROW 
 BEGIN
	 INSERT INTO activities (user_id, activity_type_id, activity_id) VALUES (
		NEW.from_user_id,
	 	(SELECT id FROM target_types tt where tt.name = 'likes'),
	 	NEW.id
	 );
 END //
 
 CREATE TRIGGER add_media_to_activities AFTER INSERT ON messages
 FOR EACH ROW 
 BEGIN
	 INSERT INTO activities (user_id, activity_type_id, activity_id) VALUES (
		NEW.from_user_id,
	 	(SELECT id FROM target_types tt where tt.name = 'media'),
	 	NEW.id
	 );
 END //
 DELIMITER ;