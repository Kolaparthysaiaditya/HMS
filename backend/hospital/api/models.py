from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)

    class Meta:
            db_table = "department"

    def __str__(self):
        return self.department_name


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    registration_date = models.DateField()

    class Meta:
            db_table = "patient"

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    class Meta:
        db_table = "doctor"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, default="Scheduled")

    class Meta:
            db_table = "appointment"

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"


class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )
    diagnosis = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255, blank=True)
    record_date = models.DateField()

    class Meta:
            db_table = "medicalrecord"

    def __str__(self):
        return self.diagnosis


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()

    class Meta:
            db_table = "medicine"

    def __str__(self):
        return self.medicine_name


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE
    )
    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE
    )
    dosage = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)

    class Meta:
            db_table = "prescription"

    def __str__(self):
        return f"{self.record} - {self.medicine}"


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    medicine_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    bill_date = models.DateField()
    payment_status = models.CharField(
        max_length=20,
        default="Pending"
    )

    class Meta:
            db_table = "bill"

    def __str__(self):
        return f"Bill {self.bill_id}"