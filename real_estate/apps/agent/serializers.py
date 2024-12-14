# Agent app serializers
from real_estate.apps.main.serializers import UserSerializer
from .models import Agent

class AgentSerializer(UserSerializer):
    user_class = Agent
    class Meta:
        model = Agent