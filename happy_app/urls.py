from django.urls import path
from .views import render_home
from .views import render_reg

urlpatterns = [
    path("buttons", render_home, name = "buttons"),
    path("reg", render_reg, name = "reg"),
]
