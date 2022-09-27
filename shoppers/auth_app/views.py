from django.shortcuts import render
from .serializers import UserSerializer
# from django.contrib.auth.models import User
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from .permissions import MyIsAuthenticatedOrReadOnly,MyIsAdminUser
# Create your views here.



class SignupAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
