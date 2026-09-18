USE hospital_management;

-- 1. Departments
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100)
);

-- 2. Patients
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    address VARCHAR(255),
    registration_date DATE NOT NULL
);

-- 3. Doctors
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE,
    department_id INT NOT NULL,

    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 4. Appointments
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'Scheduled',

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id)
);

-- 5. Medical Records
CREATE TABLE medical_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis VARCHAR(255) NOT NULL,
    treatment VARCHAR(255),
    record_date DATE NOT NULL,

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
        REFERENCES doctors(doctor_id)
);

-- 6. Medicines
CREATE TABLE medicines (
    medicine_id INT PRIMARY KEY AUTO_INCREMENT,
    medicine_name VARCHAR(100) NOT NULL UNIQUE,
    manufacturer VARCHAR(100),
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL
);

-- 7. Prescriptions
CREATE TABLE prescriptions (
    prescription_id INT PRIMARY KEY AUTO_INCREMENT,
    record_id INT NOT NULL,
    medicine_id INT NOT NULL,
    dosage VARCHAR(100),
    duration VARCHAR(100),

    FOREIGN KEY (record_id)
        REFERENCES medical_records(record_id),

    FOREIGN KEY (medicine_id)
        REFERENCES medicines(medicine_id)
);

-- 8. Bills
CREATE TABLE bills (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_id INT,
    consultation_fee DECIMAL(10,2) DEFAULT 0,
    medicine_fee DECIMAL(10,2) DEFAULT 0,
    total_amount DECIMAL(10,2) NOT NULL,
    bill_date DATE NOT NULL,
    payment_status VARCHAR(20) DEFAULT 'Pending',

    FOREIGN KEY (patient_id)
        REFERENCES patients(patient_id),

    FOREIGN KEY (appointment_id)
        REFERENCES appointments(appointment_id)
);