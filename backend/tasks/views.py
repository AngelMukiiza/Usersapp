from django.shortcuts import render

# Create your views here.
from rest_framework import generics,filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination



class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):  # Ensure this class exists
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Custom Pagination Class (Optional)
class TaskPagination(PageNumberPagination):
    page_size = 2  # Customize the number of tasks per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all().order_by("id")  # Ensure consistent ordering
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date']
