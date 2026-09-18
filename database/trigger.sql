USE hospital_management;

DELIMITER //

CREATE TRIGGER prevent_negative_stock
BEFORE UPDATE ON medicines
FOR EACH ROW
BEGIN

    IF NEW.stock_quantity < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Medicine stock cannot be negative';
    END IF;

END //

DELIMITER ;