from django.urls import path
from . import views

app_name = 'momentsapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cakes/', views.cakes, name='cakes'),
    path('contact/', views.contact, name='contact'),
]
