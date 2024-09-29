from django.urls import path
from . import views

urlpatterns = [
    path('', views.musician_list, name='musician_list'),
    path('musician/<int:id>/edit/', views.musician_edit, name='musician_edit'),
    path('musician/new/', views.musician_edit, name='musician_edit'),
    path('album/<int:id>/edit/', views.album_edit, name='album_edit'),
    path('album/new/', views.album_edit, name='album_edit'),
    path('musician/<int:id>/delete/', views.musician_delete, name='musician_delete'),
    path('album/<int:id>/delete/', views.album_delete, name='album_delete'),
]
