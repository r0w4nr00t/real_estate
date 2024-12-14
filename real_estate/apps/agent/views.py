from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from .serializers import AgentSerializer
from real_estate.utils import mailer
from rest_framework.response import Response
from real_estate.apps.property.models import Property
from real_estate.apps.property.serializers import PropertySerializer
from django.contrib.auth import authenticate

class AgentSignupView(generics.CreateAPIView):
    """ 
    Signup a new agent/broker/photographer to the system
    """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = AgentSerializer
    
    def create(self, request, *args, **kwargs):
        """ 
        Create an agent instance
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return serializer.data, headers
        
    def post(self, request, *args, **kwargs):
        serializer_data, headers = self.create(self, request, *args, **kwargs)
        # generate activation token
        # send welcome email to user with activation token
        success, id = mailer.send_welcome_message(serializer_data['email'], serializer_data['name'], activation_token=None)
        if success:
            # save email under sent emails
            return Response(serializer_data, status=status.HTTP_201_CREATED, headers=headers)
        return Response({'error': 'failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        ...
        
class AgentLoginView(APIView):
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
 
# ==================
# Dashboard
# ==================

class IndexView:
    """ 
    An overview view which displays various reports about the agent's properties and personal site
    
    """
class PropertyListView(viewsets.ReadOnlyModelViewSet):
    """ 
    Dashboard view of the the properties list
    
    """
    serializer_class =   PropertySerializer
    def get_queryset(self):
        return Property.objects.filter(agent__id=self.user.id)

class PropertyCreateUpdateView:
    ...
    
class CategoryListView:
    ...

class CategoryDetailView:
    ...

class PropertyLookupView:
    ...

