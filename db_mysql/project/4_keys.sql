-- Внешние ключи

ALTER TABLE reception 
	ADD CONSTRAINT reception_status_id_fk
		FOREIGN KEY (status_id) REFERENCES statuses(id),
	ADD CONSTRAINT reception_client_id_fk
		FOREIGN KEY (client_id) REFERENCES clients(id),
	ADD CONSTRAINT reception_object_id_fk
		FOREIGN KEY (object_id) REFERENCES objects(id),
	ADD CONSTRAINT reception_responsible_admin_id_fk
		FOREIGN KEY (responsible_admin_id) REFERENCES staff(id),
	ADD CONSTRAINT reception_responsible_master_id_fk
		FOREIGN KEY (responsible_master_id) REFERENCES staff(id);
		
ALTER TABLE staff
	ADD CONSTRAINT staff_position_id_fk
		FOREIGN KEY (position_id) REFERENCES positions(id);
		
ALTER TABLE objects
	ADD CONSTRAINT objects_object_type_id_fk
		FOREIGN KEY (object_type_id) REFERENCES object_types(id),
	ADD CONSTRAINT objects_material_type_id_fk
		FOREIGN KEY (material_type_id) REFERENCES material_types(id),
	ADD CONSTRAINT objects_photo_id_fk
		FOREIGN KEY (photo_id) REFERENCES photos(id);
		
ALTER TABLE store
	ADD CONSTRAINT store_repair_parts_id_fk
		FOREIGN KEY (repair_parts_id) REFERENCES repair_parts(id);
		
ALTER TABLE payments 
	ADD CONSTRAINT payments_payment_type_id_fk
		FOREIGN KEY (payment_type_id) REFERENCES payment_types(id),
	ADD CONSTRAINT payments_reception_id_fk
		FOREIGN KEY (reception_id) REFERENCES reception(id);
		
ALTER TABLE works 
	ADD CONSTRAINT works_object_id_fk
		FOREIGN KEY (object_id) REFERENCES objects(id),
	ADD CONSTRAINT works_master_id_fk
		FOREIGN KEY (master_id) REFERENCES staff(id),
	ADD CONSTRAINT works_work_type_id_fk
		FOREIGN KEY (work_type_id) REFERENCES work_types(id);
		
-- Индексы
	
CREATE INDEX clients_email_idx ON clients(email);

CREATE INDEX clients_phone_idx ON clients(phone);

CREATE INDEX clients_last_name_idx ON clients(last_name);

CREATE INDEX clients_last_name_first_name_idx ON clients(last_name, first_name);

CREATE INDEX objects_brand_name_idx ON objects(brand_name);

CREATE INDEX objects_brand_name_№_idx ON objects(brand_name, №);