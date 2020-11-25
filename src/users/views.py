from django.contrib.auth import get_user_model
from rest_framework import generics
from .serizlizers import UserCreateSerializer

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

