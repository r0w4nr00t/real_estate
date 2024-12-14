from django.db import models
from django.contrib.auth import get_user_model
from real_estate.apps.main.abstract_models import CustomAbstractUser

AuthUserModel = get_user_model()

# Create your models here.

class Agent(AuthUserModel):
    """ 
    Agent user model holds data about agents, brockers, filmaker and
    all user who own properties/catlogue on the site
    
    Inherits from the User model defined in the main app
    """
    
    # more Agent model fields
    ...
