from django.contrib import admin
from django.urls import path, include
from posts.views import create_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_page)
]

