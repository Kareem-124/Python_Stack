from django.urls import path     
from . import views

app_name = 'the_wall_app'
urlpatterns = [

    path('', views.index),                                       
    path('success', views.success),                                       
    path('reg_process', views.reg_process, name='reg_process'),                                       
    path('login_process', views.login, name='login_process'),                                       
    path('logout_process', views.logout, name='logout_process'),                                       
    path('msg_process', views.msg_process, name='msg_process'),                                       
    path('comment_process', views.comment_process, name='comment_process'),                                       


]