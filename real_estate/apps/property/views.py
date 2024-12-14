from django.shortcuts import render
from rest_framework import (
    status,
    generics,
    viewsets
)
from .models import Property
from .serializers import PropertySerializer

class PropertyListView(generics.ListCreateAPIView): 
    """
    Broswe all propertites in the catalog
    endpoint: /properties/
    """
    queryset= Property.objects.all()
    serializer_class = PropertySerializer
    pass

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    """
    Retrieve, update, or delete a property instance
    endpoint: /properties/<str:pk>

    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    pass 