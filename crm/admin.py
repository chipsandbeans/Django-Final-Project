from django.contrib import admin
from .models import Meal
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):

    list_display = ('title', 'protein', 'carbs', 'fats', 'meal_time', 'user')
    search_fields = ['title']
    list_filter = ('meal_time',)
    summernote_fields = ('content',)
# Register your models here.
