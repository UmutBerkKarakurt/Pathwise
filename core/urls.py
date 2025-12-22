from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_router, name="root"),         # NEW: siteye girince önce burası çalışacak
    path("welcome/", views.welcome, name="welcome"),  # NEW: hoş geldin sayfası

    path("dashboard/", views.dashboard, name="dashboard"),  # dashboard tek route
    path("courses/", views.courses, name="courses"),
    path("outcomes/", views.outcomes, name="outcomes"),
    path("students/", views.students, name="students"),
    path("home/", views.home, name="home"),
    path("ace/", views.ace, name="ace"),
]
