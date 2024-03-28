from rest_framework import serializers


class BedtimeSerializer(serializers.Serializer):
    bedtimeId = serializers.IntegerField()
    child = serializers.SerializerMethodField()
    sleepStart = serializers.DateTimeField()
    sleepEnd = serializers.DateTimeField()
    success = serializers.BooleanField()
    isNap = serializers.BooleanField()
    
    def get_child(self, obj):
        serializer = ChildSerializer(obj.child)
        return serializer.data

class ChildSerializer(serializers.Serializer):
    childId = serializers.IntegerField()
    name = serializers.CharField()
        
class PrizeSerializer(serializers.Serializer):
    prizeId = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    imageUrl = serializers.CharField()
    priority = serializers.IntegerField()
