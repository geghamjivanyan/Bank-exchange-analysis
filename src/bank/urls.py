from django.urls import path

from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('scrap/', views.scrap),
    path('graphic', views.graphic)    
]

