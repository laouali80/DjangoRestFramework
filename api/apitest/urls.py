from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.usersInfo, name='users'),
    path('user/<int:id>/', views.userDetail, name='user-detail'),
    path('create-user/', views.userCreate, name='create-user'),
    path('update-user/<int:id>/', views.userUpdate, name='update-user'),
    # path('update-user/', views.userUpdate, name='update-user'),
    path('delete-user/<int:id>/', views.userDelete, name='delete-user'),
]