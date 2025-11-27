from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'email', 'name',
        ]
        
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'required': True,
                'style': {'input_type': 'password'} 
            },
            'username': {'required': True}, 
        }
        read_only_fields = ('id',) 