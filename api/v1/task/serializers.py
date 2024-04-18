from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    
    class Meta:
        model = models.User
        fields = [
            'username',
            'password',
        ]

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user
    

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = [
            'author',
            'name',
            'file',
            'sharing',
            'group',
        ]