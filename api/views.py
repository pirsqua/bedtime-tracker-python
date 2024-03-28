from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BedtimeSerializer, ChildSerializer, PrizeSerializer
from .services import BedtimeService, ChildService, PrizeService


class BedtimeViewSet(viewsets.ViewSet):
    def list(self, request):
        bedtime_dtos = BedtimeService.get_all_bedtimes()
        serializer = BedtimeSerializer(bedtime_dtos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        bedtime_dto = BedtimeService.get_bedtime_by_id(pk)
        serializer = BedtimeSerializer(bedtime_dto)
        return Response(serializer.data)

    def create(self, request):
        child_id = request.data['childId']
        sleep_start = request.data['sleepStart']
        sleep_end = request.data['sleepEnd']
        success = request.data['success']
        is_nap = request.data['isNap']
        
        bedtime_dto = BedtimeService.create_bedtime(child_id, sleep_start, sleep_end, success, is_nap)
        serializer = BedtimeSerializer(bedtime_dto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChildViewSet(viewsets.ViewSet):
    def list(self, request):
        child_dtos = ChildService.get_all_children()
        serializer = ChildSerializer(child_dtos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        child_dto = ChildService.get_child_by_id(pk)
        serializer = ChildSerializer(child_dto)
        return Response(serializer.data)

    def create(self, request):
        name = request.data['name']
        
        child_dto = ChildService.create_child(name)
        serializer = ChildSerializer(child_dto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PrizeViewSet(viewsets.ViewSet):
    def list(self, request):
        prize_dtos = PrizeService.get_all_prizes()
        serializer = PrizeSerializer(prize_dtos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        prize_dto = PrizeService.get_prize_by_id(pk)
        serializer = PrizeSerializer(prize_dto)
        return Response(serializer.data)

    def create(self, request):
        name = request.data['name']
        description = request.data['description']
        image_url = request.data['imageUrl']
        priority = request.data['priority']
        
        prize_dto = PrizeService.create_prize(name, description, image_url, priority)
        serializer = PrizeSerializer(prize_dto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
