from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField

class CustomAbstractUser(AbstractUser):
    email = models.EmailField(
        verbose_name= "email address",
        max_length= 255,
        unique=True,
        primary_key=True
    )
    phone_number = models.PositiveIntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["phone_number"]
    
    class Meta:
        abstract =True
        get_latest_by = "date_joined"
