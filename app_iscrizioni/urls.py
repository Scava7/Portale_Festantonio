from django.urls import path
from . import views

urlpatterns = [
    path('app_iscrizioni/', views.view_iscrizioni, name='iscrizioni_tornei'),
    path('app_iscrizioni/details/<int:id>', views.view_details, name='details'),
]