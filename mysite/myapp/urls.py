from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artistIndex, name='artistIndex'),
    path('artists/<slug:first_name>/<slug:last_name>/', views.artistpage, name='artistpage'),
]