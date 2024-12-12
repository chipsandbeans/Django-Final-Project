from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import Meal, WeightTracking
from .forms import WeightTrackingForm
from django.contrib.messages.views import SuccessMessageMixin


# View Meal List
class MealListView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'crm/meal_list.html'
    context_object_name = 'meals'
    login_url = reverse_lazy('custom-login-message')

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)


# View Meal Details
class MealDetailView(DetailView):
    model = Meal
    template_name = 'crm/meal_detail.html'
    context_object_name = 'meal'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to view this meal.")
        return obj


# Create Meals
class MealCreateView(CreateView):
    model = Meal
    template_name = 'crm/meal_form.html'
    fields = ['title', 'protein', 'carbs', 'fats']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Meal created successfully!')
        return super().form_valid(form)


# Update Meals
class MealUpdateView(UpdateView):
    model = Meal
    template_name = 'crm/update_meal.html'
    fields = ['title', 'protein', 'carbs', 'fats']
    success_url = reverse_lazy('home')

# Makes sure only the meal creator can update the meal

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to update this.")
        return obj

    # Adds a message after the meal is updated
    def form_valid(self, form):
        messages.success(self.request, 'Meal updated successfully.')
        return super().form_valid(form)

    # Redirects to the meal detail page
    def get_success_url(self):
        return reverse_lazy('meal-detail', kwargs={'pk': self.object.pk})


# Meal Delete View
class MealDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Meal
    template_name = 'crm/meal_confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Meal deleted successfully!"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to delete this.")
        return obj


# Custom Log In page for users who are not signed in
def not_logged_in(user):
    return not user.is_authenticated


@user_passes_test(not_logged_in, login_url='home')
def custom_login_message(request):
    return render(request, 'crm/custom_login_message.html')


def not_logged_in(user):
    return not user.is_authenticated


# Signup for logged out users
@user_passes_test(not_logged_in, login_url='home')
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# Create a Weight Entry
class WeightCreateView(LoginRequiredMixin, CreateView):
    model = WeightTracking
    template_name = "add_weight.html"
    form_class = WeightTrackingForm
    success_url = reverse_lazy('weight_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Weight added successfully!')
        return super().form_valid(form)


# Weight List for logged in users
@method_decorator(login_required(login_url='/custom-weight-login-message/'), name='dispatch')
class WeightListView(View):
    def get(self, request):
        weights = WeightTracking.objects.filter(user=request.user)
        return render(request, 'weight_list.html', {'weights': weights})


def not_logged_in(user):
    return not user.is_authenticated


@user_passes_test(not_logged_in, login_url='weight_list')
def custom_weight_login_message(request):
    return render(request, 'custom_weight_login_message.html')


# Update Weight
@method_decorator(login_required, name='dispatch')
class WeightUpdateView(LoginRequiredMixin, UpdateView):
    model = WeightTracking
    form_class = WeightTrackingForm
    template_name = 'update_weight.html'

    # Only users can edit their weight
    def get_queryset(self):
        return WeightTracking.objects.filter(user=self.request.user)

    # Return to weight list once updated
    def form_valid(self, form):
        messages.success(self.request, 'Weight updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('weight_list')


# Delete Weight Entry
class WeightDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = WeightTracking
    template_name = 'delete_weight.html'
    success_url = reverse_lazy('weight_list')
    success_message = "Weight Entry deleted successfully!"

    def get_queryset(self):
        return WeightTracking.objects.filter(user=self.request.user)


# Custom logout view that displays logout message
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You have been successfully logged out.")
        return response


# Custom Login View that redirects logged in users to the meal list
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
