from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles_list, name="profiles_list"),
    path("add/", views.add_profile, name="add_profile"),
]
