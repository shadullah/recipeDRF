from rest_framework import serializers
from .models import ratings
class ratings(serializers.ModelSerializer):
    class Meta:
        model = ratings
        fields ='__all__'