from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from .views import (MealListView, MealDetailView, MealCreateView, MealUpdateView, MealDeleteView, custom_login_message, signup)

urlpatterns = [
    # path('meals/', views.meal_list, name='meal-list'),
    path('', MealListView.as_view(), name='home'),
    path('custom-login-message/', custom_login_message, name='custom-login-message'),
    path('signup/', signup, name='signup'),
    path('<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    path('create/', MealCreateView.as_view(), name='meal-create'),
    path('<int:pk>/update/', MealUpdateView.as_view(), name='meal-update'),
    path('<int:pk>/delete/', MealDeleteView.as_view(), name='meal-delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('weight/add/', views.WeightCreateView.as_view(), name='weight_create'),
    path('weights/', views.WeightListView.as_view(), name='weight_list'),
    path('weight/update/<int:pk>/', views.WeightUpdateView.as_view(), name='weight_update'),
    path('weight/delete/<int:pk>/', views.WeightDeleteView.as_view(), name='weight_delete'),
]