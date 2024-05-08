from rest_framework import serializers
from .models import Colours

class ColoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ['id', 'name', 'description']