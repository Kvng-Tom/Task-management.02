from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Board, Tasks
from .serializers import BoardSerializer, TaskSerializer


class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(creator=user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class BoardDeleteView(generics.DestroyAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(creator=user)
    
    
    def destroy(self, request, *args, **kwargs):
        board = self.get_object()
        board.delete()
        return Response({"message": "Board deleted successfully!"}, status=status.HTTP_200_OK)

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['completed', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority', 'created_at']

    def get_queryset(self):
        board_id = self.kwargs.get('board_id')
        return Tasks.objects.filter(board__id=board_id, board__creator=self.request.user)

    def perform_create(self, serializer):
        board_id = self.kwargs.get('board_id')
        board = Board.objects.get(id=board_id, creator=self.request.user)
        serializer.save(board=board)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        board_id = self.kwargs.get('board_id')
        return Tasks.objects.filter(board__id=board_id, board__creator=self.request.user)

    
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