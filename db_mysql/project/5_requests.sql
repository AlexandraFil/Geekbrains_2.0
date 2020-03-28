-- Вывод остатков запчастей, с нулевым количесвом выводятся в конце.

SELECT * FROM store 
	ORDER BY 
		stock = 0,
		stock;
		
-- Средний возраст сотрудников
	
SELECT 
	AVG(TIMESTAMPDIFF(YEAR, birthdate, NOW())) AS age
FROM 
	staff;
	
-- Сотрудники, чьи дни рождения в марте и апреле

SELECT birthdate, first_name, last_name
	FROM staff 
		WHERE DATE_FORMAT(birthdate, '%M') IN ('march', 'april')
			ORDER BY RIGHT(birthdate, 4);
			
-- Поиск всех заказов, выданных клиенту, но неоплаченных(без JOIN) 
-- Выводит имя и фамилию клиента, объект, заказ по которому не оплачен, номер телефона клиента
		
SELECT 
   (SELECT CONCAT(last_name, ' ', first_name)  FROM clients WHERE id = client_id) AS client, 
   (SELECT brand_name FROM objects WHERE id = object_id) AS obj,
   (SELECT phone  FROM clients WHERE id = client_id) AS phone
FROM reception 
	WHERE paid = 0 
		AND status_id = (SELECT id FROM statuses WHERE name = 'выдано клиенту');	

-- Поиск всех объектов, принадлежащих клиенту по имени и фамилии клиента
SELECT brand_name, №, reference FROM objects WHERE id IN
	(SELECT object_id FROM reception WHERE client_id = 
	(SELECT id FROM clients WHERE last_name = 'Lindgren' and first_name = 'Marcos'));


-- JOIN запрос по фамилии клиетна Lindgren позволяет увидеть все объекты, которые он приносил на ремонт, 
-- кто из мастеров проводил работы и какие работы, 
-- дату проведения работ и их статус

SELECT clients.last_name AS client_last_name, 
	clients.first_name AS client_first_name,
	objects.brand_name, 
	object_types.name AS obj_type,
	statuses.name AS status,
	staff.last_name AS master,
	work_types.name AS works,
	works.created_at AS date
	FROM clients 
		JOIN reception 
			ON clients.id = reception.client_id 
		JOIN objects 
			ON reception.object_id = objects.id 
		JOIN object_types 
			ON objects.object_type_id = object_types.id
		JOIN statuses 
			ON reception.status_id = statuses.id 
		JOIN works 
			ON objects.id = works.object_id 
		JOIN staff 
			ON works.master_id = staff.id 
		JOIN work_types 
			ON works.work_type_id = work_types.id 
	WHERE clients.last_name = 'Lindgren';
			
-- Сколько заказов у каждого мастера

SELECT staff.last_name, staff.first_name ,
	COUNT(works.master_id) AS total_works
	FROM staff
		JOIN works
			ON staff.id = works.master_id 
	GROUP BY works.master_id 
	ORDER BY total_works des;

-- Сколько заказов в ремонте у каждого мастера на данный момент

SELECT staff.last_name, staff.first_name ,
	COUNT(works.master_id) AS total_current
	FROM staff
		JOIN works
			ON staff.id = works.master_id 
		JOIN objects 
			ON works.object_id = objects.id
		JOIN reception 
			ON objects.id = reception.object_id 
		JOIN statuses 
			ON reception.status_id = statuses.id
	WHERE statuses.name = 'в ремонте'
	GROUP BY works.master_id 
	ORDER BY total_current;

-- Количество готовых, но не выданных заказов по типам объекта

SELECT object_types.name,
	COUNT(objects.object_type_id) AS total_done
	FROM reception 
		JOIN objects
			ON reception.object_id = objects.id
		JOIN object_types 
			ON objects.object_type_id = object_types.id
		JOIN statuses 
			ON reception.status_id = statuses.id
	WHERE statuses.name = 'готово'
	GROUP BY objects.object_type_id
	ORDER BY total_done;

	