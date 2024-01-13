from django.urls import path
from . import views
urlpatterns = [
    path('content/', views.content),
    path('about/', views.about)
]
