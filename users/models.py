from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    class GenderType(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
    
    class User_Type(models.TextChoices):
        PATIENT = 'Patient'
        NURSE = 'Nurse'
        DOCTOR = 'Doctor'


    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50 , blank=True)
    gender = models.CharField(max_length=50 , choices=GenderType.choices)
    birth_date = models.DateTimeField(blank=True, null=True)
    user_type = models.CharField(max_length=50 , choices=User_Type.choices)
    activation_code = models.CharField(max_length=50, blank=True)
    reset_pass_token = models.CharField(max_length=50 , blank=True)
    reset_pass_expire_date = models.DateTimeField(null=True , blank=True) 


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username



class DoctorNurseProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='doctor_profile')
    price = models.IntegerField( blank=True, null=True)
    experience_year = models.IntegerField(blank=True, null=True)
    about = models.TextField(max_length=500, blank=True)
    certificates = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"profile {self.id} for {str(self.user)}"


class PatientProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='patient_profile')
    chronic_diseases = models.TextField(blank=True)
    
    def __str__(self):
        return f"profile {self.id} for {str(self.user)}"


@receiver(post_save , sender=User)
def profile(instance , created ,  *args, **kwargs):
    if created :
        if instance.user_type == User.User_Type.PATIENT :
            PatientProfile.objects.create(
                user = instance           
            )
        
        if instance.user_type in [User.User_Type.NURSE, User.User_Type.DOCTOR] :
            DoctorNurseProfile.objects.create(
                user = instance
            )