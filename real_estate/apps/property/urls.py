# urls for the property
from django.urls import path
from .views import PropertyDetailView, PropertyListView

urlpatterns = [
    # all urls here are prefixed with properties
    path('', PropertyListView.as_view(), name='properties'),
    path("<str:pk>/",PropertyDetailView.as_view(), name="property_detail"),
]
