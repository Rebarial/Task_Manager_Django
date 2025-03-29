from django.urls import path, include
from .views import index,addTask
from .api import  TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('', index, name="planner"),
    path('addTask/', addTask, name="addTask"),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]