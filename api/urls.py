# urls.py

from django.urls import path
from .views import (
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ProjectCreateAPIView,
    ProjectListAPIView
)

urlpatterns = [
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-delete'),
    path('clients/<int:pk>/projects/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
]
