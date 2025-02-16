from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewset,
    DoctorCreate,
    DoctorList,
    DoctorRetrieve,
    DoctorDestroy,
    AppointmentCreate,
    AppointmentList,
    AppointmentDestroy,
    AppointmentUpdate,
    doctor_appointments
)

doctor_router = DefaultRouter()
doctor_router.register('doctor-viewset', DoctorViewset)


urlpatterns = [
    path('doctor/', DoctorCreate.as_view(), name='doctor-create'),
    path('doctor/all/', DoctorList.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorRetrieve.as_view(), name='doctor-detail'),
    path('doctor/delete/<int:pk>/', DoctorDestroy.as_view(), name='doctor-delete'),
    path('appointment/', AppointmentCreate.as_view(), name='appointment-create'),
    path('appointment/all/', AppointmentList.as_view(), name='appointment-list'),
    path('appointment/delete/<int:pk>/', AppointmentDestroy.as_view(), name='appointment-delete'),
    path('appointment/<int:pk>/', AppointmentUpdate.as_view(), name='appointment-update'),
    path('doctorappointments/<int:pk>/', doctor_appointments, name='doctor-appointments')
]

urlpatterns += doctor_router.urls
