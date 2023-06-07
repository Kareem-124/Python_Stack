from django.urls import path     
from . import views
app_name = 'blogs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('/new', views.new, name = 'new'),
    path('/create', views.create, name = 'create'),
    path('/<int:id>', views.show, name = 'show'),
    path('/<int:id>/edit', views.edit_num, name = 'edit_num'),
    path('/<int:id>/delete', views.destroy, name = 'destroy'),

]