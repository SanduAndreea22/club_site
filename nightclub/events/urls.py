from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('events/', views.events_view, name='events'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('menu/', views.menu_view, name='menu'),
    path('contact/', views.contact_view, name='contact'),
    path('reservations/', views.reservations_view, name='reservations'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]

