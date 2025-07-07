from django.urls import path
from.views import *



urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='tasks_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='tasks_detail'),
    path('tasks/<int:pk>/complete/', ChangeTaskStatusView.as_view(), name='tasks_complete'),
]