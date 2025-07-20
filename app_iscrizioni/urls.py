from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_main, name='main'),
    path('app_iscrizioni/', views.view_iscrizioni, name='iscrizioni_tornei'),
    path('TestPage/', views.view_testpage, name='iscrizioni_tornei'),
    path('app_iscrizioni/details/<slug:slug>', views.view_details, name='details'),
]