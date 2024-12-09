from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.utils.crypto import get_random_string



class User(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    username =models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_image',blank=True, null=True)
    phone = models.CharField(max_length=50 , blank=True)
    address = models.CharField(max_length=100 , blank=True)
    gander = models.BooleanField()
    activation_code = models.CharField(max_length=50, blank=True)
    reset_pass_token = models.CharField(max_length=50 , blank=True)
    reset_pass_expire_date = models.DateTimeField(null=True , blank=True) 



    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self) -> str:
        return self.email
