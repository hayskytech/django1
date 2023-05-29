from django.urls import path
from . import views,students,students_list
from django.urls import include


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("students", students.main, name="students"),
    path("students_list", students_list.main, name="students_list"),
]