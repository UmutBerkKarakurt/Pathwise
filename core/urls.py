from django.urls import path
from .views import home
from .views import ace

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home_alt"),
    path("ace/", ace, name="ace"),
]
