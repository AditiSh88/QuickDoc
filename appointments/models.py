from django.db import models
from django.contrib.auth.models import User

# Doctor Model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

# Patient Model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

# Appointment Model
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='Scheduled')
    
    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} on {self.appointment_time}"
