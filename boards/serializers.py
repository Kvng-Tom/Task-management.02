from rest_framework import serializers
from .models import Tasks
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
   
    title = serializers.CharField(required=True)

    class Meta:
        model = Tasks
        fields = "__all__"
        read_only_fields = ['user']

    def validate_title(self, value):
       
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        
        return value

    def validate_due_date(self, value):
        
        if value and value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
       
        return value
