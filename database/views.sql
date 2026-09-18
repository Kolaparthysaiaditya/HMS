USE hospital_management;

-- View showing complete appointment information

CREATE VIEW appointment_details AS
SELECT
    a.appointment_id,
    p.name AS patient_name,
    d.name AS doctor_name,
    dep.department_name,
    a.appointment_date,
    a.appointment_time,
    a.status
FROM appointments a
JOIN patients p
    ON a.patient_id = p.patient_id
JOIN doctors d
    ON a.doctor_id = d.doctor_id
JOIN departments dep
    ON d.department_id = dep.department_id;