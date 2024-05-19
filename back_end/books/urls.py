from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NovelViewSet

router = DefaultRouter()
router.register(r'novels', NovelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
