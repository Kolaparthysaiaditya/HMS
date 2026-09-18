USE hospital_management;

-- Departments
INSERT INTO departments
(department_name, location)
VALUES
('Cardiology', 'Block A'),
('Neurology', 'Block B'),
('Orthopedics', 'Block C'),
('General Medicine', 'Block A'),
('Pediatrics', 'Block D');


-- Patients
INSERT INTO patients
(name, age, gender, phone, address, registration_date)
VALUES
('Rahul Sharma', 35, 'Male', '9876543210', 'Hyderabad', '2026-01-10'),
('Priya Reddy', 28, 'Female', '9876543211', 'Vijayawada', '2026-01-12'),
('Arjun Kumar', 45, 'Male', '9876543212', 'Kakinada', '2026-01-15'),
('Sneha Rao', 22, 'Female', '9876543213', 'Visakhapatnam', '2026-01-18'),
('Ravi Teja', 52, 'Male', '9876543214', 'Rajahmundry', '2026-01-20');


-- Doctors
INSERT INTO doctors
(name, specialization, phone, department_id)
VALUES
('Dr. Anil Kumar', 'Cardiologist', '9000000001', 1),
('Dr. Meena Rao', 'Neurologist', '9000000002', 2),
('Dr. Suresh Reddy', 'Orthopedic Surgeon', '9000000003', 3),
('Dr. Kavya Sharma', 'General Physician', '9000000004', 4),
('Dr. Priyanka Das', 'Pediatrician', '9000000005', 5);


-- Appointments
INSERT INTO appointments
(patient_id, doctor_id, appointment_date, appointment_time, status)
VALUES
(1, 1, '2026-02-01', '10:00:00', 'Completed'),
(2, 2, '2026-02-02', '11:00:00', 'Completed'),
(3, 3, '2026-02-03', '12:00:00', 'Scheduled'),
(4, 4, '2026-02-04', '09:30:00', 'Completed'),
(5, 5, '2026-02-05', '14:00:00', 'Scheduled');


-- Medical Records
INSERT INTO medical_records
(patient_id, doctor_id, diagnosis, treatment, record_date)
VALUES
(1, 1, 'High Blood Pressure', 'Medication and regular monitoring', '2026-02-01'),
(2, 2, 'Migraine', 'Pain management and rest', '2026-02-02'),
(3, 3, 'Knee Pain', 'Physiotherapy', '2026-02-03'),
(4, 4, 'Fever', 'Medication and rest', '2026-02-04'),
(5, 5, 'Cold and Cough', 'Syrup and tablets', '2026-02-05');


-- Medicines
INSERT INTO medicines
(medicine_name, manufacturer, price, stock_quantity)
VALUES
('Paracetamol', 'ABC Pharma', 20.00, 100),
('Amlodipine', 'HealthCare Ltd', 50.00, 80),
('Ibuprofen', 'MediLife', 30.00, 60),
('Cetirizine', 'PharmaPlus', 15.00, 120),
('Omeprazole', 'ABC Pharma', 40.00, 90);


-- Prescriptions
INSERT INTO prescriptions
(record_id, medicine_id, dosage, duration)
VALUES
(1, 2, '5 mg once daily', '30 days'),
(2, 3, '400 mg twice daily', '5 days'),
(3, 3, '400 mg once daily', '7 days'),
(4, 1, '500 mg twice daily', '5 days'),
(5, 4, '10 mg once daily', '5 days');


-- Bills
INSERT INTO bills
(patient_id, appointment_id, consultation_fee, medicine_fee, total_amount, bill_date, payment_status)
VALUES
(1, 1, 500.00, 50.00, 550.00, '2026-02-01', 'Paid'),
(2, 2, 600.00, 30.00, 630.00, '2026-02-02', 'Paid'),
(3, 3, 500.00, 30.00, 530.00, '2026-02-03', 'Pending'),
(4, 4, 400.00, 20.00, 420.00, '2026-02-04', 'Paid'),
(5, 5, 400.00, 15.00, 415.00, '2026-02-05', 'Pending');