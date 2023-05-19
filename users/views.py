from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from users.serializers import UserCreateSerializers, UserAuthorizeSerializers, UserConfirmSerializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from random import randint
from rest_framework.generics import CreateAPIView, DestroyAPIView


class AuthorizeAPIView(CreateAPIView):
    serializer_class = UserAuthorizeSerializers
    lookup_field = 'id'
    def post(self, request, *args, **kwargs):
        serialize = UserAuthorizeSerializers(data=request.data)
        serialize.is_valid(raise_exception=True)
        username = serialize.validated_data.get('username')
        password = serialize.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def confirm_api_view(request):
#     serializers = UserConfirmSerializers(data=request.data)
#     serializers.is_valid(raise_exception=True)
#     cod = serializers.validated_data.get('cod')
#     correct_cod = randint(100000, 999999)
#     if cod == correct_cod:
#         user = User.objects.create(cod=cod)
#         return Response(data={'user_id': user.id})
#     else:
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializers.errors)




class RegisterAPIViews(CreateAPIView):
    serializer_class = UserCreateSerializers
    lookup_field = 'id'
    def post(self, request, *args, **kwargs):
        serializers = UserCreateSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        return Response(data={'user_id': user.id})




