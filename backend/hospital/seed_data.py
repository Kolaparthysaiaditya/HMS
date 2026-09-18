from datetime import date, time
from api.models import (
    Department,
    Patient,
    Doctor,
    Appointment,
    MedicalRecord,
    Medicine,
    Prescription,
    Bill,
)

# -----------------------------
# Departments
# -----------------------------

departments_data = [
    ("Cardiology", "Block A"),
    ("Neurology", "Block B"),
    ("Orthopedics", "Block C"),
    ("General Medicine", "Block A"),
    ("Pediatrics", "Block D"),
]

departments = {}

for name, location in departments_data:
    department, _ = Department.objects.get_or_create(
        department_name=name,
        defaults={"location": location},
    )
    departments[name] = department


# -----------------------------
# Patients
# -----------------------------

patients_data = [
    ("Rahul Sharma", 35, "Male", "9876543210", "Hyderabad", date(2026, 1, 10)),
    ("Priya Reddy", 28, "Female", "9876543211", "Vijayawada", date(2026, 1, 12)),
    ("Arjun Kumar", 45, "Male", "9876543212", "Kakinada", date(2026, 1, 15)),
    ("Sneha Rao", 22, "Female", "9876543213", "Visakhapatnam", date(2026, 1, 18)),
    ("Ravi Teja", 52, "Male", "9876543214", "Rajahmundry", date(2026, 1, 20)),
]

patients = {}

for name, age, gender, phone, address, registration_date in patients_data:
    patient, _ = Patient.objects.get_or_create(
        phone=phone,
        defaults={
            "name": name,
            "age": age,
            "gender": gender,
            "address": address,
            "registration_date": registration_date,
        },
    )
    patients[phone] = patient


# -----------------------------
# Doctors
# -----------------------------

doctors_data = [
    ("Dr. Anil Kumar", "Cardiologist", "9000000001", "Cardiology"),
    ("Dr. Meena Rao", "Neurologist", "9000000002", "Neurology"),
    ("Dr. Suresh Reddy", "Orthopedic Surgeon", "9000000003", "Orthopedics"),
    ("Dr. Kavya Sharma", "General Physician", "9000000004", "General Medicine"),
    ("Dr. Priyanka Das", "Pediatrician", "9000000005", "Pediatrics"),
]

doctors = {}

for name, specialization, phone, department_name in doctors_data:
    doctor, _ = Doctor.objects.get_or_create(
        phone=phone,
        defaults={
            "name": name,
            "specialization": specialization,
            "department": departments[department_name],
        },
    )
    doctors[phone] = doctor


# -----------------------------
# Appointments
# -----------------------------

appointments_data = [
    ("9876543210", "9000000001", date(2026, 2, 1), time(10, 0), "Completed"),
    ("9876543211", "9000000002", date(2026, 2, 2), time(11, 0), "Completed"),
    ("9876543212", "9000000003", date(2026, 2, 3), time(12, 0), "Scheduled"),
    ("9876543213", "9000000004", date(2026, 2, 4), time(9, 30), "Completed"),
    ("9876543214", "9000000005", date(2026, 2, 5), time(14, 0), "Scheduled"),
]

appointments = {}

for (
    patient_phone,
    doctor_phone,
    appointment_date,
    appointment_time,
    status,
) in appointments_data:

    appointment, _ = Appointment.objects.get_or_create(
        patient=patients[patient_phone],
        doctor=doctors[doctor_phone],
        appointment_date=appointment_date,
        appointment_time=appointment_time,
        defaults={
            "status": status,
        },
    )

    appointments[(patient_phone, doctor_phone)] = appointment


# -----------------------------
# Medical Records
# -----------------------------

records_data = [
    (
        "9876543210",
        "9000000001",
        "High Blood Pressure",
        "Medication and regular monitoring",
        date(2026, 2, 1),
    ),
    (
        "9876543211",
        "9000000002",
        "Migraine",
        "Pain management and rest",
        date(2026, 2, 2),
    ),
    (
        "9876543212",
        "9000000003",
        "Knee Pain",
        "Physiotherapy",
        date(2026, 2, 3),
    ),
    (
        "9876543213",
        "9000000004",
        "Fever",
        "Medication and rest",
        date(2026, 2, 4),
    ),
    (
        "9876543214",
        "9000000005",
        "Cold and Cough",
        "Syrup and tablets",
        date(2026, 2, 5),
    ),
]

records = {}

for (
    patient_phone,
    doctor_phone,
    diagnosis,
    treatment,
    record_date,
) in records_data:

    record, _ = MedicalRecord.objects.get_or_create(
        patient=patients[patient_phone],
        doctor=doctors[doctor_phone],
        diagnosis=diagnosis,
        record_date=record_date,
        defaults={
            "treatment": treatment,
        },
    )

    records[(patient_phone, doctor_phone)] = record


# -----------------------------
# Medicines
# -----------------------------

medicines_data = [
    ("Paracetamol", "ABC Pharma", 20.00, 100),
    ("Amlodipine", "HealthCare Ltd", 50.00, 80),
    ("Ibuprofen", "MediLife", 30.00, 60),
    ("Cetirizine", "PharmaPlus", 15.00, 120),
    ("Omeprazole", "ABC Pharma", 40.00, 90),
]

medicines = {}

for name, manufacturer, price, stock_quantity in medicines_data:
    medicine, _ = Medicine.objects.get_or_create(
        medicine_name=name,
        defaults={
            "manufacturer": manufacturer,
            "price": price,
            "stock_quantity": stock_quantity,
        },
    )
    medicines[name] = medicine


# -----------------------------
# Prescriptions
# -----------------------------

prescriptions_data = [
    ("9876543210", "9000000001", "Amlodipine", "5 mg once daily", "30 days"),
    ("9876543211", "9000000002", "Ibuprofen", "400 mg twice daily", "5 days"),
    ("9876543212", "9000000003", "Ibuprofen", "400 mg once daily", "7 days"),
    ("9876543213", "9000000004", "Paracetamol", "500 mg twice daily", "5 days"),
    ("9876543214", "9000000005", "Cetirizine", "10 mg once daily", "5 days"),
]

for (
    patient_phone,
    doctor_phone,
    medicine_name,
    dosage,
    duration,
) in prescriptions_data:

    Prescription.objects.get_or_create(
        record=records[(patient_phone, doctor_phone)],
        medicine=medicines[medicine_name],
        defaults={
            "dosage": dosage,
            "duration": duration,
        },
    )


# -----------------------------
# Bills
# -----------------------------

bills_data = [
    (
        "9876543210",
        "9000000001",
        500.00,
        50.00,
        550.00,
        date(2026, 2, 1),
        "Paid",
    ),
    (
        "9876543211",
        "9000000002",
        600.00,
        30.00,
        630.00,
        date(2026, 2, 2),
        "Paid",
    ),
    (
        "9876543212",
        "9000000003",
        500.00,
        30.00,
        530.00,
        date(2026, 2, 3),
        "Pending",
    ),
    (
        "9876543213",
        "9000000004",
        400.00,
        20.00,
        420.00,
        date(2026, 2, 4),
        "Paid",
    ),
    (
        "9876543214",
        "9000000005",
        400.00,
        15.00,
        415.00,
        date(2026, 2, 5),
        "Pending",
    ),
]

for (
    patient_phone,
    doctor_phone,
    consultation_fee,
    medicine_fee,
    total_amount,
    bill_date,
    payment_status,
) in bills_data:

    appointment = appointments[(patient_phone, doctor_phone)]

    Bill.objects.get_or_create(
        patient=patients[patient_phone],
        appointment=appointment,
        defaults={
            "consultation_fee": consultation_fee,
            "medicine_fee": medicine_fee,
            "total_amount": total_amount,
            "bill_date": bill_date,
            "payment_status": payment_status,
        },
    )


print("Hospital sample data inserted successfully!")