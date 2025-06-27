from rest_framework import serializers
from .models import Board, Tasks


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ['creator']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
        read_only_fields = ['board']