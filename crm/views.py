from django.shortcuts import render
from .models import Meal

def meal_list(request):
    # Fetch meals that belong to the current logged-in user
    meals = Meal.objects.filter(user=request.user)
    
    return render(request, 'meal_list.html', {'object_list': meals})
