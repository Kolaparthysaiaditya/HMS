USE hospital_management;


-- ==========================================
-- 1. BASIC SELECT QUERIES
-- ==========================================

-- Display all patients
SELECT * FROM patients;

-- Display all doctors
SELECT * FROM doctors;

-- Display all departments
SELECT * FROM departments;


-- ==========================================
-- 2. WHERE CLAUSE
-- ==========================================

-- Find patients older than 40
SELECT *
FROM patients
WHERE age > 40;


-- Find female patients
SELECT *
FROM patients
WHERE gender = 'Female';


-- ==========================================
-- 3. ORDER BY
-- ==========================================

-- Display patients from oldest to youngest
SELECT *
FROM patients
ORDER BY age DESC;


-- ==========================================
-- 4. INNER JOIN
-- ==========================================

-- Display doctors with their departments
SELECT
    d.doctor_id,
    d.name AS doctor_name,
    d.specialization,
    dep.department_name
FROM doctors d
JOIN departments dep
ON d.department_id = dep.department_id;


-- ==========================================
-- 5. MULTIPLE TABLE JOIN
-- ==========================================

-- Display appointment details
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
ON a.doctor_id = d.doctor_id;


-- ==========================================
-- 6. AGGREGATE FUNCTIONS
-- ==========================================

-- Count total patients
SELECT COUNT(*) AS total_patients
FROM patients;


-- Find average patient age
SELECT AVG(age) AS average_age
FROM patients;


-- Find maximum patient age
SELECT MAX(age) AS maximum_age
FROM patients;


-- Find minimum patient age
SELECT MIN(age) AS minimum_age
FROM patients;


-- Calculate total hospital billing
SELECT SUM(total_amount) AS total_revenue
FROM bills;


-- ==========================================
-- 7. GROUP BY
-- ==========================================

-- Count doctors in each department
SELECT
    dep.department_name,
    COUNT(d.doctor_id) AS doctor_count
FROM departments dep
LEFT JOIN doctors d
ON dep.department_id = d.department_id
GROUP BY dep.department_id, dep.department_name;


-- Count patients by gender
SELECT
    gender,
    COUNT(*) AS patient_count
FROM patients
GROUP BY gender;


-- ==========================================
-- 8. HAVING
-- ==========================================

-- Departments having more than one doctor
SELECT
    dep.department_name,
    COUNT(d.doctor_id) AS doctor_count
FROM departments dep
JOIN doctors d
ON dep.department_id = d.department_id
GROUP BY dep.department_id, dep.department_name
HAVING COUNT(d.doctor_id) > 1;


-- ==========================================
-- 9. SUBQUERY
-- ==========================================

-- Find patients older than the average patient age
SELECT *
FROM patients
WHERE age > (
    SELECT AVG(age)
    FROM patients
);


-- ==========================================
-- 10. DISTINCT
-- ==========================================

-- Display unique patient genders
SELECT DISTINCT gender
FROM patients;


-- ==========================================
-- 11. LIKE
-- ==========================================

-- Find patients whose names start with 'R'
SELECT *
FROM patients
WHERE name LIKE 'R%';


-- ==========================================
-- 12. BETWEEN
-- ==========================================

-- Find patients between age 25 and 50
SELECT *
FROM patients
WHERE age BETWEEN 25 AND 50;


-- ==========================================
-- 13. BILL REPORT
-- ==========================================

SELECT
    p.name AS patient_name,
    b.consultation_fee,
    b.medicine_fee,
    b.total_amount,
    b.payment_status
FROM bills b
JOIN patients p
ON b.patient_id = p.patient_id;


-- ==========================================
-- 14. PENDING BILLS
-- ==========================================

SELECT
    p.name AS patient_name,
    b.total_amount,
    b.payment_status
FROM bills b
JOIN patients p
ON b.patient_id = p.patient_id
WHERE b.payment_status = 'Pending';