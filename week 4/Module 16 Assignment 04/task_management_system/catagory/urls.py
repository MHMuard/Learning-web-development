from django.urls import path
from .views import create_catagory
urlpatterns = [
    path('create_catagory/', create_catagory, name='create_catagory'),
]
