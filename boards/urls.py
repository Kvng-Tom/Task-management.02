from django.urls import path
from.views import *



urlpatterns = [
    path('boards/', BoardListCreateView.as_view()),
    path('boards/<int:pk>/', BoardDeleteView.as_view()),
    path('boards/<int:board_id>/tasks/', TaskListCreateView.as_view()),
    path('boards/<int:board_id>/tasks/<int:pk>/', TaskDetailView.as_view()),
]