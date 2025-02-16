from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    office = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.specialty}"
    
class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    
