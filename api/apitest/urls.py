from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.usersInfo, name='users'),
    path('users/<int:id>/', views.userDetail, name='user-detail'),
    # path('newUser/', views.createUser, name='create-user'),
    # path('users/<int:id>/', views.updateUser, name='update-user'),
    # path('delete/<int:id>/', views.deleteUser, name='delete-user'),
]