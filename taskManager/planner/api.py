from .models import Task
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import TaskSerialazer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects
    serializer_class = TaskSerialazer
    # permission_classes = (IsAuthenticatedOrReadOnly)
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user = user)
        return queryset

    def get_tasks_for_user(user):
        user = user
        queryset = Task.objects.filter(user = user)
        return queryset



"""class TaskAPIList(generics.ListCreateAPIView):
    queryset= Task.objects.all()
    serializer_class = TaskSerialazer

class TaskAPIUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialazer

class TaskAPIDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerialazer"""

"""class PlannerAPIView(APIView):
    def get(self, request):
        task = Task.objects.all()
        return Response({'Tasks': TaskSerialazer(task, many=True).data})

    def post(self, requset):
        serializer = TaskSerialazer(data=requset.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TaskSerialazer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request,*args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        instance.delete()

        return Response({"post": f"delete post {pk}"})"""