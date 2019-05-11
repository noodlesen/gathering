from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('number/<int:num>/', views.number, name='number'),
    path('feed', views.feed, name='feed'),
]