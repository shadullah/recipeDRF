from django.shortcuts import render
from rest_framework import viewsets
from .models import ratings
from . import serializers


# Create your views here.
class UserListView(viewsets.ModelViewSet):
    queryset = ratings.objects.all()
    serializer_class = serializers.UserlistSerializer