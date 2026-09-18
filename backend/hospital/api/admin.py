from django.contrib import admin
from .models import (
    Department,
    Patient,
    Doctor,
    Appointment,
    MedicalRecord,
    Medicine,
    Prescription,
    Bill,
)


admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Bill)