from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorViewset,
    DoctorCreate,
    DoctorList,
    DoctorRetrieve,
    DoctorDestroy
)

doctor_router = DefaultRouter()
doctor_router.register('doctor-viewset', DoctorViewset)


urlpatterns = [
    path('doctor/', DoctorCreate.as_view(), name='doctor-create'),
    path('doctor/all/', DoctorList.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorRetrieve.as_view, name='doctor-detail')
]

urlpatterns += doctor_router.urls
