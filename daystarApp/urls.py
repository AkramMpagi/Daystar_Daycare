from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dolls/', views.dolls, name='dolls'),
    path('babies/', views.baby, name='baby'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('sitters/', views.sitters, name='sitters'),
    path('sitter_registration/', views.sitter_registration, name='sitter_registration'),
    path('baby_registration/', views.baby_registration, name='baby_registration'),


]

    
 

