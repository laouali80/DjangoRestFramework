from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.usersInfo, name='users'),
    path('users/<int:id>/', views.userDetail, name='user-detail'),
    path('create/', views.userCreate, name='create-user'),
    path('users/<int:id>/', views.userUpdate, name='update-user'),
    # path('update-user/', views.userUpdate, name='update-user'),
    path('user/<int:id>/', views.userDelete, name='delete-user'),
]