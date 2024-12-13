from django.shortcuts import render
from .models import About


# Get the most recently updated object
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    return render(request, 'about_us/about.html', {'about_us': about})
