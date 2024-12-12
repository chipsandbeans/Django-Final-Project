from django.contrib import admin
from .models import Meal, WeightTracking
from django_summernote.admin import SummernoteModelAdmin


# Meal Class
@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):

    list_display = ('title', 'protein', 'carbs', 'fats', 'meal_time', 'user')
    search_fields = ['title']
    list_filter = ('meal_time',)
    summernote_fields = ('content',)


admin.site.register(WeightTracking)


# Weight Class
class Weight(SummernoteModelAdmin):
    list_display = ('user', 'weight', 'date')
    list_filter = ['date', ]
    summernote_fields = ('content',)
