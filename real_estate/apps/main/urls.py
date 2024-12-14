#urls for the main app

from django.urls import path 
from .views import Healthz


urlpatterns = [
    path("healthz/", Healthz.as_view(), name="main"),    
]