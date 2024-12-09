from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Meal, WeightTracking
from .forms import WeightTrackingForm

class MealListView(LoginRequiredMixin, ListView):
    model = Meal 
    template_name = 'crm/meal_list.html'
    context_object_name = 'meals'
    login_url = reverse_lazy('custom-login-message')

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class MealDetailView(DetailView):
    model = Meal
    template_name = 'crm/meal_detail.html'
    context_object_name = 'meal'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to view this meal.")
        return obj

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

# Custom Log In message for users who are not signed in
def custom_login_message(request):
    return render(request, 'crm/custom_login_message.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class WeightCreateView(LoginRequiredMixin, CreateView):
    model = WeightTracking
    template_name = "add_weight.html"
    form_class = WeightTrackingForm
    success_url = reverse_lazy('weight_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required(login_url='/custom-weight-login-message/'), name='dispatch')
class WeightListView(View):
    def get(self, request):
        weights = WeightTracking.objects.filter(user=request.user)
        return render(request, 'weight_list.html', {'weights': weights})

def custom_weight_login_message(request):
    return render(request, 'custom_weight_login_message.html')

class WeightUpdateView(LoginRequiredMixin, UpdateView):
    model = WeightTracking
    form_class = WeightTrackingForm
    template_name = 'update_weight.html'

    # Only users can edit their weight
    def get_queryset(self):
        return WeightTracking.objects.filter(user=self.request.user)

    # Return to weight list once updated
    def get_success_url(self):
        return reverse_lazy('weight_list')

class WeightDeleteView(DeleteView):
    model = WeightTracking
    template_name = "delete_weight.html"
    success_url = reverse_lazy('weight_list')

    def get_queryset(self):
        return WeightTracking.objects.filter(user=self.request.user)