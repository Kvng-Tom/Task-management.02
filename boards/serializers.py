from rest_framework import serializers
from .models import Board, Tasks
from datetime import datetime


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


    def validate_title(self, value):
        if not value.strip:
            raise serializers.ValidationError("Title cannot be empty.")
    
    def validate_due_date(self, value):
        if value and value < datetime.now():
            raise serializers.ValidationError("Due date cannot be in the past.")