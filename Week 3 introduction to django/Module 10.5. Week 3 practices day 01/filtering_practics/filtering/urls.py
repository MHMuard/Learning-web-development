from django.urls import path
from . import views

urlpatterns = [
    path('geeks/', views.geeksforgeeks),
    path('earthly/', views.earthly)
]
