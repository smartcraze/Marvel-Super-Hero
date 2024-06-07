from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.superhero, name='Superhero'),

]