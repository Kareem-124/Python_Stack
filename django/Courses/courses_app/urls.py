from django.urls import path     
from . import views

app_name = 'courses_app'
urlpatterns = [

    path('', views.index, name='home_page'),                                       
    path('add_course', views.add_course, name='add_course'),                                       
    path('comment_page/<int:id>', views.comment_page, name='comment_page'),                                       
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),                                       

]