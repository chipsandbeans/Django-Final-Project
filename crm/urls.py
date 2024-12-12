from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import (
    MealListView, MealDetailView, MealCreateView, MealUpdateView,
    MealDeleteView, custom_login, signup, WeightListView,
    WeightCreateView, WeightUpdateView, WeightDeleteView,
    CustomLogoutView, CustomLoginView
)


urlpatterns = [
    # path('meals/', views.meal_list, name='meal-list'),
    path('', MealListView.as_view(), name='home'),
    path('custom-login/', custom_login, name='custom-login'),
    path('signup/', signup, name='signup'),
    path('<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    path('create/', MealCreateView.as_view(), name='meal-create'),
    path('<int:pk>/update/', MealUpdateView.as_view(), name='meal-update'),
    path('<int:pk>/delete/', MealDeleteView.as_view(), name='meal-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('weights/', views.WeightListView.as_view(), name='weight_list'),
    path('weight/add/', WeightCreateView.as_view(), name='create_weight'),
    path('weight/update/<int:pk>/', views.WeightUpdateView.as_view(), name='weight_update'),
    path('weight/delete/<int:pk>/', views.WeightDeleteView.as_view(), name='weight_delete'),
    path('my-weight/', WeightListView.as_view(), name='weight_list'),
    path('my-weight/', views.WeightListView.as_view(), name='weight_list'),
    path('add-weight/', WeightCreateView.as_view(), name='add_weight'),
    path('custom-login2/', views.custom_login2, name='custom-login2'),
]
