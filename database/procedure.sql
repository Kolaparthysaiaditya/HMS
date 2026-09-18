USE hospital_management;

DELIMITER //

CREATE PROCEDURE GetPatientAppointments(IN p_patient_id INT)
BEGIN

    SELECT
        a.appointment_id,
        p.name AS patient_name,
        d.name AS doctor_name,
        a.appointment_date,
        a.appointment_time,
        a.status
    FROM appointments a

    JOIN patients p
        ON a.patient_id = p.patient_id

    JOIN doctors d
        ON a.doctor_id = d.doctor_id

    WHERE a.patient_id = p_patient_id;

END //

DELIMITER ;