from .views import RoomViewSet, DeviceViewSet

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]