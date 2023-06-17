from django.urls import path     
from . import views

app_name = 'login_and_rej'
urlpatterns = [

    path('', views.index),                                       
    path('success', views.success),                                       
    path('reg_process', views.reg_process, name='reg_process'),                                       
    path('login_process', views.login, name='login_process'),                                       
    path('logout_process', views.logout, name='logout_process'),                                       


]