from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('dolls/', views.dolls, name='dolls'),
    path('babies/', views.baby, name='baby'),
    path('payment/', views.payment, name='payment'),
    path('contact/', views.contact, name='contact'),
    path('sitters/', views.sitters, name='sitters'),
    path('sitter_registration/', views.sitter_registration, name='sitter_registration'),
    path('baby_registration/', views.baby_registration, name='baby_registration'),
    path('doll_store/', views.doll_store, name='doll_store'),
    path('doll_sales/', views.doll_sales, name='doll_sales'),
    path('otherplay_tools/', views.otherplay_tools, name='otherplay_tools'),
    path('doll/', views.doll, name='doll'),
    path('invoices/', views.invoices, name='invoices'),
    path('all_transactions/', views.all_transactions, name='all_transactions'),
    # path('login/', views.login_user, name='login'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('result_detail/<int:result_id>/', views.result_detail, name='result_detail'),
    path('edit_sitter/<int:sitter_id>/', views.edit_sitter, name='edit_sitter'),

#  path('logout/', auth_views.LogoutView.as_view(template_name = 'products/logout.html'), name = 'logout' ),
  

    
         


]

    
 

