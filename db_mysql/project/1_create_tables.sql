/*База данных создана для использования сотрудниками часовой мастерской.
 *Основной является таблица reception (список актов приемки), она включает 
 *данные о клиенте; объекте, переданном в мастерскую на ремонт; необходимых запчастях;
 *ответственных за прием мастера и администратора; 
 *статус заказа - принято/в ремонте/готово/выдано.
 *
 *Таблица works содержит данные о том, 
 *какой мастер прооводит работу с объектом и какой тип работ он выполняет.
 * 
 *Таблицы clients, objects, staff содержат необходимую информацию 
 *о клиентах, объектах, сотрудниках мастерской.
 *
 *Таблица payments отображает прошедшие оплаты по номерам приема объектов на ремонт 
 *(reception_id).
 * 
 *Таблица store отображает наличие запчастей на складе.
 *Она не привязана к другим таблицам, поскольку не все заказы требуют запчастей, и 
 *требуемых запчастей может не быть на складе. Однако в reception.repair_parts_id
 *могут быть указаны store.id
 *
 *В проекте создано 7 sql файлов, они пронумерованны в порядке создания.
 *
 *1_create_tables - первоначальное создание таблиц
 *2_fill_tables - наполнение фейковыми данными
 *3_CRUD - редактирование данных в таблицах
 *4_keys - внешние ключи и индексы
 *5_requests - некоторые выборки
 *6_trigger_func - хранимые операции
 *7_window_view - запрос через оконную функцию, представления
 */


CREATE DATABASE watch_service;

USE watch_service;

CREATE TABLE clients (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	phone VARCHAR(15) NOT NULL,
	email VARCHAR(120) NOT NULL,
	discount INT UNSIGNED,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

CREATE TABLE store (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	repair_parts_id INT UNSIGNED,
	vendor_code VARCHAR(100) NOT NULL, #артикул
	price DECIMAL,
	stock INT UNSIGNED
);

CREATE TABLE repair_parts (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE reception (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	status_id INT UNSIGNED,
	client_id INT UNSIGNED,
	object_id INT UNSIGNED,
	paid BOOLEAN,
	responsible_admin_id INT UNSIGNED,
	responsible_master_id INT UNSIGNED,
	comment TEXT,
	repair_parts_requested INT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

CREATE TABLE statuses (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE objects (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	object_type_id INT UNSIGNED,
	brand_name VARCHAR(100) NOT NULL,
	№ VARCHAR(20),
	reference VARCHAR(20),
	material_type_id INT UNSIGNED,
	photo_id INT UNSIGNED
);

CREATE TABLE object_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE material_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE photos (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	filename VARCHAR(255) NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

CREATE TABLE payments (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	reception_id INT UNSIGNED,
	total DECIMAL,
	payment_type_id INT UNSIGNED,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

CREATE TABLE payment_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE staff (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	phone VARCHAR(15) NOT NULL,
	position_id INT UNSIGNED,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT NOW() ON UPDATE NOW()
);

CREATE TABLE positions (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE works (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	object_id INT UNSIGNED,
	master_id INT UNSIGNED,
	comment TEXT,
	work_type_id INT UNSIGNED,
	created_at DATETIME DEFAULT NOW()
);

CREATE TABLE work_types (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL UNIQUE
);

SHOW TABLES;

