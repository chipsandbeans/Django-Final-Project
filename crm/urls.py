from . import views
from django.urls import path

urlpatterns = [
    path('meals/', views.meal_list, name='meal-list'),
    ]