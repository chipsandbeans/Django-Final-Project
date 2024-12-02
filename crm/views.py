from django.shortcuts import render
from django.views import generic
from .models import Meal

"""
def meal_list(request):
    # Fetch meals that belong to the current logged-in user
    meals = Meal.objects.filter(user=request.user)
    template_name = "crm/index.html"
    paginate_by = 6
    
    return render(request, 'meal_list.html', {'object_list': meals})
"""

def meal_list(request):
    meals = Meal.objects.all()  # Retrieve all meals
    return render(request, 'meal_list.html', {'meals': meals})