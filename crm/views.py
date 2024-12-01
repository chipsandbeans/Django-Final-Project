from django.shortcuts import render
from .models import Meal

def meal_list(request):
    # Fetch meals that belong to the current logged-in user
    meals = Meal.objects.filter(user=request.user)  # Filter meals by the logged-in user
    
    # Render the template and pass the meals to the context
    return render(request, 'meal_list.html', {'object_list': meals})
