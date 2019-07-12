from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstartapp.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    查看、编辑用户数据的API接口
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer