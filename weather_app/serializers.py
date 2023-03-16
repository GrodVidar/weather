from rest_framework import serializers
from .models import HeatIndex


class HeatIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatIndex
        fields = ('date', 'temperature', 'humidity')
