from django.db import models
from django.contrib.auth.models import User

class VaccineLocation(models.Model):
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    address = models.CharField(max_length=30)
    clinic_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    register_link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.clinic_name}: {self.address[:9]}, {self.city}"

class Vote(models.Model):
    location = models.ForeignKey(VaccineLocation, on_delete=models.CASCADE, default=None)
    score = models.IntegerField()
    created_date = models.DateField()
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Appointment(models.Model):
    location = models.ForeignKey(VaccineLocation, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)#(fulfilled, pending, missed)
    reason = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    appointment_made_date = models.DateField()
    appointment_finished_date = models.DateField(null=False)

    @property
    def wait_time(self):
        if self.status == "Complete":
            return self.appointment_made_date - appointment_finished_date
        else:
            return None