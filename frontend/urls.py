from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.landing_page, name='landing-page'),
	path('contact/', views.contact_us, name='contact-page'),
	path('about/', views.about_us, name='about-page'),
    path('login/', views.login_redirect, name='login-redirect'),
    path('solutions/', views.solutions, name='solutions-page'),
] 
