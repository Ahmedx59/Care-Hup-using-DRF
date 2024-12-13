from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderType(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50 , blank=True)
    gender = models.CharField(max_length=50 , choices=GenderType.choices)
    birth_date = models.DateTimeField(blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username



class DoctorNurseProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='doctor_profile')
    price = models.IntegerField()
    experience_year = models.IntegerField()
    about = models.TextField(max_length=500)
    certificates = models.TextField(max_length=500)


class PatientProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='patient_profile')
    chronic_diseases = models.TextField()