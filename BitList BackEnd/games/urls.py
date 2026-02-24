from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

router = DefaultRouter()
router.register(r'my-games', GameViewSet, basename='game')

urlpatterns = [
    path('', include(router.urls)),
]