from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_claim/', views.add_claim, name='add_claim'),
    path('update_progress/<int:claim_id>/', views.update_progress, name='update_progress'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]