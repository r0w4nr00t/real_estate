from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from real_estate.apps.main.abstract_models import CustomAbstractUser

AuthUserModel = get_user_model()

class Customer(AuthUserModel):
    """ 
    Customer user model
    Inherits from the User model defined in the main app
    """
    
    # more customer model fields
    ...
    
