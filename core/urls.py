from django.contrib import admin
from django.urls import path, include
from posts.views import main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main)
]

