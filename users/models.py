from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50 , blank=True)
    gender = models.BooleanField()
    birth_date = models.DateTimeField()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]



class Doctor(AbstractUser):
    price = models.IntegerField()
    experience_year = models.IntegerField()
    about = models.TextField(max_length=500)
    certificates = models.TextField(max_length=500)


class Patient(AbstractUser):
    chronic_diseases = models.TextField()