from django.urls import path
from . import views  

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('add/', views.add_user, name='users_list')
]