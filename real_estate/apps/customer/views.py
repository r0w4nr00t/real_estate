from django.shortcuts import render
from rest_framework import (
    generics, 
    status,
    viewsets,
)
from .models import Customer
from .serializers import CustomerSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.base import View

class AccountSummaryView(generics.RetrieveAPIView):
    """
    Gets called when a user clicks the 'Account' page in the nav bar
     
    """
    ...
    
class CustomerSignupView(generics.CreateAPIView)  :
    """ 
    Allows customers to register for a new account
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CustomerSerializer
    ...

class CustomerLoginView(APIView):
    permission_classes = ()
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token":user.auth_token.key})   
        else:
            return Response({"error":"wrong credentials"}, status=status.HTTP_400_BAD_REQUEST) 
        pass
    ...
    
class LogoutView:
    ...

# =============
# Profile
# =============
class ProfileViewSet(viewsets.ModelViewSet):
    """ 
    Allow customers to view and or update their credentials 
    """
    ...

class ChangePasswordView:
    ...

# =================
# Order History
# ==================

class OrderHistoryView:
    """ 
    All customer order history view
    """
    ...
class OrderDetialView:
    """ 
    View history about a specific order 
    """
    



