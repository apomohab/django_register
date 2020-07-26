from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    #post views
    
    #path('login/', views.user_login, name='login'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    
    #password changes
    
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'), #built in function no need views
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'), #built in function no need views
    
    #reset password
    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #register
    path('register/', views.register, name='register'),
    
    
    
    
    
]