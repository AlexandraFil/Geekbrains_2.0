SHOW TABLES;

-- users, profiles

DESC users;
SELECT * FROM users;

UPDATE users SET created_at = updated_at WHERE created_at > updated_at;

ALTER TABLE users ADD COLUMN password VARCHAR(30) NOT NULL AFTER phone;

UPDATE users SET password = '123456';

UPDATE users SET password = CONCAT(FLOOR(1 + (RAND() * 3300)), first_name) WHERE ID < 30;

UPDATE users SET password = CONCAT(phone, last_name, FLOOR(1 + (RAND() * 300))) WHERE ID > 70;

SELECT * FROM profiles LIMIT 10;

UPDATE profiles SET sex = '';

CREATE TEMPORARY TABLE sex (sex CHAR(1));

INSERT INTO sex VALUES ('m'), ('f');

SELECT * FROM sex;

UPDATE profiles SET sex = (SELECT sex FROM sex ORDER BY RAND() LIMIT 1);

SELECT COUNT(*) FROM users;

-- messages

DESC messages;

SELECT * FROM messages LIMIT 30;

UPDATE messages SET from_user_id = FLOOR(1 + (RAND() * 100));

SELECT * FROM messages WHERE from_user_id = to_user_id;

ALTER TABLE messages ADD COLUMN head VARCHAR(255) AFTER to_user_id;

# CREATE TEMPORARY TABLE heads (head VARCHAR(255));

# INSERT INTO heads VALUES ('HAPPY NEW YEAR!'), ('HAPPY BIRTHDAY!'), ('important message'), ('meeting tomorrow'), ('Cheap bananas!'), ('Spam'), ('not really important message'), ('Do not read it');

# SELECT * FROM heads;

# UPDATE messages SET head = (SELECT head FROM heads ORDER BY RAND() LIMIT 1);

UPDATE messages SET head = (SELECT head FROM posts WHERE messages.id = posts.id); 

ALTER TABLE messages ADD COLUMN to_community_id INT UNSIGNED AFTER to_user_id;

UPDATE messages SET to_community_id = FLOOR(1 + (RAND() * 10)) WHERE to_user_id > from_user_id;

-- media

SELECT * FROM media_types;

TRUNCATE media_types;

INSERT INTO media_types (name) VALUE
	('photo'),
	('video'),
	('audio');

SELECT * FROM media LIMIT 10;

SELECT COUNT(*) FROM media;

UPDATE media SET
	user_id = FLOOR(1 + (RAND() * 100)),
	media_type_id = FLOOR(1 + (RAND() * 3)),
	size = 4567 WHERE size = 0;

UPDATE media SET filename = CONCAT('https://dropbox.net/vk/file_', filename);

UPDATE media SET metadata = CONCAT('{"owner":"',
	(SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id), 
	'"}'); 

DESC media;

ALTER TABLE media  MODIFY metadata JSON;

-- friendship

SELECT * FROM friendship LIMIT 10;

SELECT COUNT(*) FROM friendship;

UPDATE friendship SET
	user_id = FLOOR(1 + (RAND() * 100)),
	status_id = FLOOR(1 + (RAND() * 3));

UPDATE friendship SET confirmed_at = requested_at WHERE requested_at  > confirmed_at;

SELECT * FROM friendship WHERE user_id = friend_id;

SELECT * FROM friendship_statuses;

TRUNCATE friendship_statuses;

INSERT INTO friendship_statuses (name) VALUE
	('Requested'),
	('Confirmed'),
	('Rejected');

-- communities

SELECT * FROM communities;

SELECT COUNT(*) FROM communities;

DELETE FROM communities WHERE id > 10;

ALTER TABLE communities ADD COLUMN is_open BOOLEAN;

ALTER TABLE communities ADD COLUMN description VARCHAR(255) AFTER name;

UPDATE communities SET is_open = TRUE WHERE id IN (1,2,5,7,9);

UPDATE communities SET is_open = FALSE WHERE is_open IS NULL;

UPDATE communities SET description = (SELECT body FROM messages WHERE messages.id = communities.id); 

SELECT * FROM communities_users;

SELECT COUNT(*) FROM communities_users;

UPDATE communities_users SET
	community_id = FLOOR(1 + (RAND() * 10));

-- Добавление новых таблиц

CREATE TABLE posts (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	media_id INT UNSIGNED,
	user_id INT UNSIGNED NOT NULL,
	head VARCHAR(255),
	body MEDIUMTEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

SELECT * FROM posts LIMIT 20;

CREATE TABLE likes (
	event_id INT UNSIGNED ,
	reviewer_id INT UNSIGNED,
	review_status_id INT UNSIGNED,
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY (event_id, reviewer_id)
);

SELECT * FROM likes LIMIT 10;

UPDATE likes SET created_at = updated_at WHERE created_at > updated_at;

-- в данной таблице content_id - это id медиа, поста или сообщения в зависимости от типа

CREATE TABLE events (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	owner_id INT UNSIGNED NOT NULL,
	event_type_id INT UNSIGNED,
	content_id INT UNSIGNED
);

SELECT * FROM events LIMIT 10;

CREATE TABLE event_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(150) NOT NULL UNIQUE
);

INSERT INTO event_types (name) VALUE
	('post'),
	('media'),
	('message');

SELECT * FROM event_types;

CREATE TABLE review_statuses (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(150) NOT NULL UNIQUE
);

INSERT INTO review_statuses (name) VALUE
	('Unwatched'),
	('Watched'),
	('Liked'),
	('Disliked');
	
SELECT * FROM review_statuses;