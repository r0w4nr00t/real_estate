from rest_framework import serializers
from .models import CustomBaseUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    user_class = CustomBaseUser #to be overrided in subclasses with the name of the model and object to be used
    class Meta:
        model = CustomBaseUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}
        pass
    
    def create(self, validated_data):
        user = self.user_class(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name =  validated_data['last_name'],
            phone_number = validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

