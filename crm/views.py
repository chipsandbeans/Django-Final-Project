from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Meal

# Shows meals if logged in, if not redirects to login
@login_required
def meal_list(request):
    user_id = request.user.id 
    meals = Meal.objects.filter(user_id=user_id)
    return render(request, 'meal_list.html', {'meals': meals})

# Create: Add a new meal 
@login_required
def meal_create(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user 
            meal.save()
            return redirect('meal-list')
    else:
        form = MealForm()
    return render(request, 'crm/meal_form.html', {'form': form, 'action': 'Create'})
