from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from random import randint



class UserAuthorizeSerializers(serializers.Serializer):
    username = serializers.CharField(min_length=3)
    password = serializers.CharField(min_length=3)

class UserCreateSerializers(UserAuthorizeSerializers):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')

class UserConfirmSerializers(serializers.Serializer):
    cod = serializers.IntegerField(min_value=100000, max_value=999999)
