from rest_framework import serializers
from .models import User
# it allows us to return a json format object

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'