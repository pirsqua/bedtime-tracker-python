from rest_framework import serializers

from .models import Bedtime, Child, Prize


class BedtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bedtime
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'
        
class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prize
        fields = '__all__'
