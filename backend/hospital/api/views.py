from django.db import connection
from datetime import date, datetime, time
from decimal import Decimal
from django.conf import settings

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

from .serializers import (
    DepartmentSerializer,
    PatientSerializer,
    DoctorSerializer,
    AppointmentSerializer,
    MedicalRecordSerializer,
    MedicineSerializer,
    PrescriptionSerializer,
    BillSerializer,
)

class SQLQueryView(APIView):

    def post(self, request):
        query = request.data.get("query", "").strip()
        passkey = request.data.get("passkey", "")

        if not query:
            return Response(
                {"error": "Please enter a SQL query."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if query.endswith(";"):
            query = query[:-1].strip()

        # Only one SQL statement
        if ";" in query:
            return Response(
                {"error": "Only one SQL query is allowed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        first_word = query.split()[0].lower()

        protected_commands = {
            "insert",
            "update",
            "delete",
            "create",
            "alter",
            "drop",
            "truncate",
            "replace",
        }

        # Passkey required for database-changing commands
        if first_word in protected_commands:

            if passkey != settings.SQL_ADMIN_PASSKEY:
                return Response(
                    {"error": "Invalid passkey."},
                    status=status.HTTP_403_FORBIDDEN
                )

        # SQLite doesn't support TRUNCATE
        if first_word == "truncate":
            return Response(
                {
                    "error":
                    "SQLite does not support TRUNCATE TABLE. "
                    "Use DELETE FROM table_name instead."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            with connection.cursor() as cursor:

                cursor.execute(query)

                if cursor.description:
                    columns = [
                        column[0]
                        for column in cursor.description
                    ]

                    rows = cursor.fetchall()

                    safe_rows = []

                    for row in rows:
                        safe_row = []

                        for value in row:
                            if isinstance(
                                value,
                                (date, datetime, time, Decimal)
                            ):
                                safe_row.append(str(value))
                            else:
                                safe_row.append(value)

                        safe_rows.append(safe_row)

                    return Response({
                        "columns": columns,
                        "rows": safe_rows,
                        "message":
                            f"{len(safe_rows)} record(s) returned."
                    })

                return Response({
                    "columns": [],
                    "rows": [],
                    "message": "SQL query executed successfully."
                })

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
# Department API
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# Patient API
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


# Doctor API
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# Appointment API
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


# Medical Record API
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


# Medicine API
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


# Prescription API
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


# Bill API
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer