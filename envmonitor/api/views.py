from .models import Device, Room
from .serializers import DeviceSerializer, RoomSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    """
    @list_route(methods=['get'], permission_classes=[permissions.AllowAny])
    def status(self, request):
        consumptions = Consumption.objects.all()
        serializer = ConsumptionSerializer(consumptions, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Consumption.objects.filter(user=self.request.user)
    """