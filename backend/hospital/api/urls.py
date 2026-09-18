from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DepartmentViewSet,
    PatientViewSet,
    DoctorViewSet,
    AppointmentViewSet,
    MedicalRecordViewSet,
    MedicineViewSet,
    PrescriptionViewSet,
    BillViewSet,
    SQLQueryView,
)

router = DefaultRouter()

router.register('departments', DepartmentViewSet)
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('appointments', AppointmentViewSet)
router.register('medical-records', MedicalRecordViewSet)
router.register('medicines', MedicineViewSet)
router.register('prescriptions', PrescriptionViewSet)
router.register('bills', BillViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('query/', SQLQueryView.as_view()),
]