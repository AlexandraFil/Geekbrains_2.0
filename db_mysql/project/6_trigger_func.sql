USE watch_service;
DESC clients;

-- Тригер, не допускающий одновременно пустых значений в полях clients.last_name, clients.first_name
-- (на данный момент на столбцы установлено NOT NUll, 
-- тригерр нужен будет при желании сделать возможным не заполнять одно из полей)

DELIMITER //

CREATE TRIGGER validate_first_name_last_name_insert BEFORE INSERT ON clients
FOR EACH ROW BEGIN
	IF NEW.first_name IS NULL AND NEW.last_name IS NULL THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Необходимо ввести имя клиента';
	END IF;
END//

CREATE TRIGGER validate_first_name_last_name_update BEFORE UPDATE ON clients
FOR EACH ROW BEGIN
	IF NEW.first_name IS NULL AND NEW.last_name IS NULL THEN
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Необходимо ввести имя клиента';
	END IF;
END//

-- Функция показывает соотношение неоплаченных заказов к общему количеству заказов от клиента

CREATE FUNCTION client_responsibility(check_client_id INT)
RETURNS FLOAT READS SQL DATA

	BEGIN
    
		DECLARE paid_orders INT;
        DECLARE total_orders INT;
        
        SET paid_orders = 
			(SELECT COUNT(*) 
				FROM reception 
					WHERE client_id = check_client_id AND paid = 1);
                    
		SET total_orders = 
			(SELECT COUNT(*) 
				FROM reception 
					WHERE client_id = check_client_id);
                    
		RETURN paid_orders / total_orders;
	END//
    
DELIMITER ;
SELECT client_responsibility(123);

                    
		