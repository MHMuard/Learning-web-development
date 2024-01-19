from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ="homepage"),
    path('ordinarycoders/', views.ordinarycoders, name = "ordinarycoders.com"),
    path('geeksforgeeks/', views.geeksforgeeks, name = "geeksforgeeks.com"),
]