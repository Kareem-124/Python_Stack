from django.urls import path     
from . import views

app_name = 'user_dash_app'
urlpatterns = [                                 
    path('', views.index, name='root_page'),                                        # Index Page

]