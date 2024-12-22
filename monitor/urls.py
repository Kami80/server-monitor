from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Main UI
    path('health/', views.health, name='health'),  # JSON API
]