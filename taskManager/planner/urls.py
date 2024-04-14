from django.urls import path, include
from .views import index
from .api import  TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', index),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]