from django.urls import path
from .views import create_page


urlpatterns = [
    path('', create_page, name='create_page')
]
