from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    protein = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    # Timestamp automatically saves time and date. 
    meal_time = models.DateTimeField(auto_now_add=True)
    # Links to the user who created the meal
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def total_calories(self):
        return (self.protein *4) + (self.carbs * 4) + (self.fats * 9)