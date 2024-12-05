from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
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
        form.instance.user = self.request.user 
        return super().form_valid(form)

class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'crm/meal_form.html'
    fields = ['title', 'protein', 'carbs', 'fats']
    success_url = reverse_lazy('home')
    
    # Makes sure only the meal creator can update the meal
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to update this meal.")
        return obj
    
    # Adds a message after the meal is updated
    def form_valid(self, form):
        messages.success(self.request, 'Meal updated successfully.')
        return super().form_valid(form)

    # Redirects to the meal detail page
    def get_success_url(self):
        return reverse_lazy('meal-detail', kwargs={'pk': self.object.pk})

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'crm/meal_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to delete this meal.")
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Meal deleted successfully.')
        return super().delete(request, *args, **kwargs)