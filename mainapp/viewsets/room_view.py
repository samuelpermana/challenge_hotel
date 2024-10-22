
from rest_framework import viewsets
from ..models.room_model import  Rooms
from mainapp.serializers.room_serializer import  RoomsSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
