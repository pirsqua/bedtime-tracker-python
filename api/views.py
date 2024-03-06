from rest_framework import viewsets
from .models import Bedtime, Child, Prize
from .serializers import BedtimeSerializer, ChildSerializer, PrizeSerializer

class BedtimeViewSet(viewsets.ModelViewSet):
    queryset = Bedtime.objects.all()
    serializer_class = BedtimeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
