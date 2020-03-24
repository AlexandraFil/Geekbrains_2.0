-- Оконные функции
-- Оценка средней стоимости работ по каждому типу объекта ремонта
                
SELECT DISTINCT object_types.name,
	AVG(payments.total) OVER w AS average,
    MIN(payments.total) OVER w AS min,
    MAX(payments.total) OVER w AS max,
	SUM(payments.total) OVER w AS total_by_type,
    SUM(payments.total) OVER() AS total,
    SUM(payments.total) OVER w / SUM(payments.total) OVER() * 100 AS "%%"
FROM payments
	JOIN reception 
		ON payments.reception_id = reception.id 
	JOIN objects 
		ON reception.object_id = objects.id 
	JOIN object_types 
		ON objects.object_type_id = object_types.id
    WINDOW w AS (PARTITION BY objects.object_type_id);
    
-- Представления

CREATE OR REPLACE VIEW staff_positions AS 
SELECT
	CONCAT(s.last_name, ' ', s.first_name) AS worker,
	s.birthdate,
	p.name AS position
FROM
	staff AS s
JOIN
	positions AS p
ON	
	s.position_id = p.id
ORDER BY RIGHT(birthdate, 5);

SHOW TABLES;

SELECT * FROM staff_positions;

CREATE OR REPLACE VIEW clients_objects AS 
SELECT 
	CONCAT(c.last_name, ' ', c.first_name) AS client,
	CONCAT(o.brand_name, ' ', o.`№`, ' ', o.reference) AS obj, 
	s.name AS status
FROM clients c 
JOIN reception r 
	ON r.client_id = c.id
JOIN objects o
	ON r.object_id = o.id
JOIN statuses s
	ON r.status_id = s.id
ORDER BY client;

SELECT * FROM clients_objects;
