from rest_framework import generics
from django.contrib.auth.models import User
from ..serializers import UserSerializer

# Views de Usuários

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer