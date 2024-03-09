import statistics
from django.contrib import admin
from django.urls import path, include

from myproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include app-specific URLs

]



