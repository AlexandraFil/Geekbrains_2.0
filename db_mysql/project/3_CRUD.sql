USE watch_service;

SHOW TABLES;

SELECT * FROM payment_types;

SELECT * FROM material_types;

TRUNCATE material_types;

INSERT INTO material_types (name) VALUES
  ('Au 750'),
  ('сталь/золото'),
  ('белое золото'),
  ('розовое золото'),
  ('steel'),
  ('керамика'),
  ('сталь/керамика'),
  ('дерево'),
  ('Ag'),
  ('Pt'),
  ('carbon'),
  ('Ti'),
  ('Ti/керамика');

SELECT * FROM object_types;

TRUNCATE object_types;

INSERT INTO object_types (name) VALUES
  ('часы наручные'),
  ('часы настенные'),
  ('часы настольные'),
  ('часы карманные'),
  ('ювелирные изделия');

SELECT * FROM clients;

UPDATE clients SET created_at = updated_at WHERE created_at > updated_at;

UPDATE clients SET phone = CONCAT('+7-9', FLOOR(10 + (RAND() * 89)), '-', FLOOR(10 + (RAND() * 89)), '-', FLOOR(10 + (RAND() * 89)));

SELECT * FROM objects LIMIT 10;

UPDATE objects SET object_type_id = FLOOR(1 + (RAND() * 5));

CREATE TEMPORARY TABLE brand_names (brand_name VARCHAR(255));

INSERT INTO brand_names VALUES ('BVLGARY'), ('EMPORIO ARMANI'), ('Луч'), ('Ракета'), ('Весна'), ('Ulysse Nardin'), ('Tissot'), ('Rado'), ('Maurice Lacroix'), ('Longines'), ('Raymond Weil'), ('Alpina'), ('Zenith'), ('Omega'), ('Rolex'), ('TAG Heuer'), ('Oris'), ('Breitling'), ('HUBLOT'), ('Chanel'), ('Tudor'), ('Baume & Mercier');

SELECT * FROM brand_names;

UPDATE objects SET brand_name = (SELECT brand_name FROM brand_names ORDER BY RAND() LIMIT 1);

UPDATE objects SET № = CONCAT(FLOOR(1 + (RAND() * 999)), '.', FLOOR(1 + (RAND() * 99)), '.', FLOOR(1 + (RAND() * 9)), FLOOR(1 + (RAND() * 999)));

UPDATE objects SET reference = CONCAT(reference, '.', FLOOR(1 + (RAND() * 99)), '.', FLOOR(1 + (RAND() * 9)), FLOOR(1 + (RAND() * 999)));

UPDATE objects SET material_type_id = FLOOR(1 + (RAND() * 13));

UPDATE objects SET photo_id = FLOOR(1 + (RAND() * 300));

SELECT * FROM photos LIMIT 10;

UPDATE photos SET filename = CONCAT('https://dropbox.net/watch_service/file_', filename);

SELECT * FROM payments LIMIT 10;

DESC payments;

UPDATE payments SET reception_id = FLOOR(1 + (RAND() * 300));

UPDATE payments SET total = CONCAT(FLOOR(1 + (RAND() * 99)), '000', '.', '00');

SELECT * FROM positions;

SELECT * FROM statuses;

SELECT * FROM staff;

ALTER TABLE staff ADD COLUMN birthdate DATE AFTER phone;

UPDATE staff SET 
	phone = CONCAT('+7-9', FLOOR(10 + (RAND() * 89)), '-', FLOOR(10 + (RAND() * 89)), '-', FLOOR(10 + (RAND() * 89))),
	position_id = FLOOR(1 + (RAND() * 4)),
	birthdate = CONCAT('19', FLOOR(70 + (RAND() * 19)), '-0', FLOOR(1 + (RAND() * 9)), '-', FLOOR(10 + (RAND() * 19)));

UPDATE staff SET position_id = 1 WHERE position_id = 3;
UPDATE staff SET position_id = 3 WHERE id IN (13, 24);
UPDATE staff SET position_id = 2 WHERE id IN (16, 21, 15);

SELECT * FROM reception;

UPDATE reception SET 
	status_id = FLOOR(1 + (RAND() * 4)),
	client_id = FLOOR(1 + (RAND() * 300)),
	object_id = FLOOR(1 + (RAND() * 700));

CREATE TEMPORARY TABLE admins (admin_id INT UNSIGNED);

INSERT INTO admins VALUES ('6'), ('8'), ('10'), ('25');

CREATE TEMPORARY TABLE masters (master_id INT UNSIGNED);

INSERT INTO masters VALUES ('1'), ('2'), ('3'), ('7');

UPDATE reception SET
	responsible_admin_id = (SELECT admin_id FROM admins ORDER BY RAND() LIMIT 1),
	responsible_master_id = (SELECT master_id FROM masters ORDER BY RAND() LIMIT 1);

UPDATE reception SET repair_parts_requested = NULL;
	
UPDATE reception SET repair_parts_requested = FLOOR(1 + (RAND() * 350)) WHERE (client_id + object_id) > 550;

SELECT * FROM repair_parts;

TRUNCATE repair_parts;

INSERT INTO repair_parts (name) VALUES
  ('ремень для часов'),
  ('браслеты для часов металлические'),
  ('заводная коронка'),
  ('кнопка хронографа'),
  ('застежка'),
  ('бакл'),
  ('винт'),
  ('стело'),
  ('камень'),
  ('колесо');

SELECT * FROM store LIMIT 10;

UPDATE store SET 
	repair_parts_id = FLOOR(1 + (RAND() * 10)),
	price = CONCAT(FLOOR(1 + (RAND() * 19)), '000', '.', '00');

TRUNCATE work_types;

INSERT INTO work_types (name) VALUES
  ('ювелирные работы'),
  ('профилактический ремонт'),
  ('полировка'),
  ('замена запчастей'),
  ('замена ремня'),
  ('замена элемента питания'),
  ('замена стекла'),
  ('изготовление винта'),
  ('замена механизма'),
  ('установка стрелок'),
  ('регулировка точности хода'),
  ('восстановление герметичности');
 
SELECT * FROM work_types;

SELECT * FROM works LIMIT 10;

UPDATE works SET object_id = FLOOR(1 + (RAND() * 700));

CREATE TEMPORARY TABLE masters (master_id INT UNSIGNED);

INSERT INTO masters VALUES ('1'), ('2'), ('3'), ('4'), ('5'), ('7'), ('9'), ('11'), ('12'), ('13'), ('14'), ('15'), ('16'), ('17'), ('18'), ('19'), ('20'), ('21'), ('22'), ('23'), ('24'), ('20'), ('23'), ('15'), ('16'), ('17'), ('18'), ('19');

UPDATE works SET
	master_id = (SELECT master_id FROM masters ORDER BY RAND() LIMIT 1);

UPDATE works SET work_type_id = FLOOR(1 + (RAND() * 12));
