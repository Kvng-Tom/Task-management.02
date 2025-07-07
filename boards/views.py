from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Tasks
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class TaskListCreateView(generics.ListCreateAPIView):
    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['completed', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority', 'created_at']

    def get_queryset(self):

        return Tasks.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
  
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
     
        task = self.get_object()
        task.delete()
        
        return Response({"message": "Task deleted successfully!"}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response({"message": "Task updated successfully!"}, status=status.HTTP_200_OK)

class ChangeTaskStatusView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Mark a task as completed",
        responses={200: "Task marked as completed", 404: "Task not found"},
    )
    def patch(self, request, pk):
        try:
            task = Tasks.objects.get(pk=pk, board__creator=request.user)
        except Tasks.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task.completed = True
        task.status = "done"  
        task.save()

        return Response({"message": "Task marked as completed"}, status=status.HTTP_200_OK)