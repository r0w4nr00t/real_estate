""" 
Agent endpoints
"""
from django.urls import path
from . views import *

urlpatterns = [
    path('<str:pk>/properties/', PropertyListView.as_view(), name='agent_properties'),
    path('register/', AgentSignupView.as_view(), name='signup'),
    path('login/', AgentLoginView.as_view(), name='login'),
]