from . import views
from django.contrib import admin
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
    ]