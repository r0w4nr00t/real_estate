# Serializers for the Customers app 

from rest_framework import serializers
from .models import Customer
from rest_framework.authtoken.models import Token
from real_estate.apps.main.serializers import UserSerializer

# extends user serializer from main
class CustomerSerializer(UserSerializer):
    user_class = Customer
    class Meta:
        model = Customer


    