# Customer urls

from django.urls import path
from .views import CustomerSignupView, CustomerLoginView, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profile/", ProfileViewSet, basename="profile")

urlpatterns = [
    path("register/", CustomerSignupView.as_view(), name="signup"),
    path('login/', CustomerLoginView.as_view(), name='login'),
]