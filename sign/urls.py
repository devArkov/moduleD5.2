from django.urls import path
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='sign/logout.html'), name='logout'),
]