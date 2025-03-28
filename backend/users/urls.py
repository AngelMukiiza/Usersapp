from django.urls import path
from .views import UserListCreate, UserDetail 

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='users_list'),  # List and create users
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # Retrieve, update, and delete a user
]
