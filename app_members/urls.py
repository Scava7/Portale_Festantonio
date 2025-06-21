from django.urls import path
from . import views

urlpatterns = [
    path('app_members/', views.view_members, name='members'),
]