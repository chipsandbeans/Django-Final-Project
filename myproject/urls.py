from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about_us.urls')), 
    path('summernote/', include('django_summernote.urls')),
    # path('', include('crm.urls'), name='home'),
    path('', include('crm.urls')),
    # path('', lambda request: redirect('meal-list')), 
    path("accounts/", include("allauth.urls")),
]
