from . import views
from django.urls import path
from .views import (MealListView, MealDetailView, MealCreateView,)

urlpatterns = [
    # path('meals/', views.meal_list, name='meal-list'),
    path('', MealListView.as_view(), name='home'),
    path('<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    path('create/', MealCreateView.as_view(), name='meal-create'),
    ]