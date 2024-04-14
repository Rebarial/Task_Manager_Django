from rest_framework import serializers
from .models import Task

class TaskSerialazer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = "__all__"


"""
class TaskSerialazer(serializers.Serializer):

    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    announce = serializers.CharField()
    date = serializers.DateField()
    time = serializers.TimeField()
    description = serializers.CharField(default="")

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.announce = validated_data.get("announce", instance.announce)
        instance.date = validated_data.get("date", instance.date)
        instance.time = validated_data.get("time", instance.time)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

"""