from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

from .models import CurrencyModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrencyModel
        fields = '__all__'