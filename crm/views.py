from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Meal

class MealListView(ListView):
    model = Meal 
    template_name = 'crm/meal_list.html'
    context_object_name = 'meals'

class MealDetailView(DetailView):
    model = Meal
    template_name = 'crm/meal_detail.html'
    context_object_name = 'meal'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'crm/meal_form.html'
    fields = ['title', 'protein', 'carbs', 'fats']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user as the logged-in user
        return super().form_valid(form)