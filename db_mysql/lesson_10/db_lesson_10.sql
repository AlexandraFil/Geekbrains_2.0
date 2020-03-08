USE vk;

DELIMITER -
CREATE FUNCTION friendship_direction(check_user_id INT)
RETURNS FLOAT READS SQL DATA

	BEGIN
		DECLARE requests_to_user INT;
        DECLARE requests_from_user INT;
        
        SET requests_to_user =
			(SELECT COUNT(*)
				FROM friendship
					WHERE friend_id = check_user_id);
                    
		SET requests_from_user =
			(SELECT COUNT(*)
				FROM friendship
					WHERE user_id = check_user_id);
                    
		RETURN requests_to_user / requests_from_user;
	END-
    
    DELIMITER ;
    
    SELECT friendship_direction(4);
    
    DELIMITER -
    
    CREATE PROCEDURE friendship_offers (IN for_user_id INT)
    
		BEGIN
			(
				SELECT pr2.user_id
					FROM profiles pr1
						JOIN profiles pr2
							ON pr1.hometown = pr2.hometown
					WHERE pr1.user_id = for_user_id
                    
				UNION
                
				SELECT cu2.user_id
					FROM communities_users cu1
						JOIN communities_users cu2
							ON cu1.community_id = cu2.community_id
					WHERE cu1.user_id = for_user_id
                    
				UNION
                
                SELECT DISTINCT fr2.user_id
					FROM friendship fr1
						JOIN friendship fr2
							ON fr1.user_id = fr2.user_id
								OR fr1.friend_id = fr2.friend_id
                                OR fr1.friend_id = fr2.user_id
                                OR fr1.user_id = fr2.friend_id
					WHERE fr1.user_id = for_user_id
						OR fr1.friend_id = for_user_id
			)
			ORDER BY RAND()
            LIMIT 5;

		END; -
        
DELIMITER ;
    
CALL friendship_offers(3);

-- INDEX
    
SELECT * FROM users ORDER BY id DESC LIMIT 50;
        
SELECT * FROM users WHERE email = 'orion.johnson@example.org';

SELECT email FROM users ORDER BY email;

SELECT * FROM media WHERE user_id = 11 AND media_type_id = 3;

CREATE INDEX users_email_idx ON users(email);

CREATE INDEX media_user_id_media_type_id_idx ON media(user_id, media_type_id); 

SHOW CREATE TABLE users;

-- Оконные функции 
-- функция OVER окно
-- () все поля запроса - наиболее общий случай

-- Задача: сколько занимают места медиафайлы по типам в процентном соотношенииalter

SELECT media_types.name,
	SUM(media.size) AS total_by_type,
    (SELECT SUM(size) FROM media) AS total_size,
    SUM(media.size)/(SELECT SUM(size) FROM media) * 100 AS "%%"
		FROM media
			JOIN media_types
				ON media.media_type_id = media_types.id
		GROUP BY media.media_type_id;
        
SELECT DISTINCT media_types.name,
	SUM(media.size) OVER(PARTITION BY media.media_type_id) AS total_by_type,
    SUM(media.size) OVER() AS total,
    SUM(media.size) OVER(PARTITION BY media.media_type_id) / SUM(media.size) OVER() * 100 AS "%%"
		FROM media
			JOIN media_types
				ON media.media_type_id = media_types.id;
                
SELECT DISTINCT media_types.name,
	AVG(media.size) OVER(PARTITION BY media.media_type_id) AS average,
    MIN(media.size) OVER(PARTITION BY media.media_type_id) AS min,
    MAX(media.size) OVER(PARTITION BY media.media_type_id) AS max,
	SUM(media.size) OVER(PARTITION BY media.media_type_id) AS total_by_type,
    SUM(media.size) OVER() AS total,
    SUM(media.size) OVER(PARTITION BY media.media_type_id) / SUM(media.size) OVER() * 100 AS "%%"
		FROM media
			JOIN media_types
				ON media.media_type_id = media_types.id;
                
SELECT DISTINCT media_types.name,
	AVG(media.size) OVER w AS average,
    MIN(media.size) OVER w AS min,
    MAX(media.size) OVER w AS max,
	SUM(media.size) OVER w AS total_by_type,
    SUM(media.size) OVER() AS total,
    SUM(media.size) OVER w / SUM(media.size) OVER() * 100 AS "%%"
		FROM (media
			JOIN media_types
				ON media.media_type_id = media_types.id)
                WINDOW w AS (PARTITION BY media.media_type_id);
                
SELECT user_id, hometown, birthday,
	ROW_NUMBER() OVER w AS 'row_number',
    FIRST_VALUE(hometown) OVER w AS 'first',
    LAST_VALUE(hometown) OVER w AS 'last',
    NTH_VALUE(hometown, 2) OVER w AS 'second'
		FROM profiles
			WINDOW w AS(PARTITION BY LEFT(birthday, 3) ORDER BY birthday);