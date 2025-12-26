from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard_alt"),
    path("courses/", views.courses, name="courses"),
    path("outcomes/", views.outcomes, name="outcomes"),
    path("students/", views.students, name="students"),
    path("home/", views.home, name="home"),
    path("ace/", views.ace, name="ace"),
    path("software/", views.software, name="software"),
]


