from django.urls import path     
from . import views
app_name = 'users_app'
urlpatterns = [
    path('', views.index),
    path('add_user', views.add_user, name= 'add_user')

]