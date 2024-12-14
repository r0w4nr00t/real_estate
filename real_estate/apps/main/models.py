from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .abstract_models import CustomAbstractUser
from django.contrib.auth import get_user_model
#from phonenumber_field.modelfields import PhoneNumberField

AuthUserModel = get_user_model()

class CustomBaseUser(CustomAbstractUser):
    ...
class Token(models.Model):
    Scope = models.TextChoices('Scope', 'ACTIVATION AUTHENTICATION')
    created_at = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, primary_key=True)
    user_id = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE) # to be set to a base class and make use of polymorphism 
    expiry = models.DateTimeField()
    scope = models.CharField(max_length=14, choices=Scope.choices)
    
    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"
    
    def __str__(self):
        return f"Token for {self.user_id} expiring on {self.expiry}"
    

