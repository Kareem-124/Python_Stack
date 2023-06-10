from django.urls import path     
from . import views

app_name = 'dojo_ninja_app'
urlpatterns = [
    path('', views.index, name='home_page'),
    path('process', views.process, name='process'),

]