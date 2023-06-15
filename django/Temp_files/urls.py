from django.urls import path     
from . import views

app_name = 'TV_Show_app'
urlpatterns = [
    path('show', views.index, name='show_page'),                                   # Add a New Book Page
    path('', views.index, name='root_page'),                                        # Add a New Book Page
    path('show/new', views.new_show, name='show_new'),                              # Add a New Book Page
    path('show/new/create', views.create_new_show, name='create_show_new'),                              # Add a New Book Page
    path('show/<int:id>', views.show_details, name='show_details'),                              # Add a New Book Page
    path('show/<int:id>/edit', views.show_edit, name='show_edit'),                              # Add a New Book Page
    path('show/<int:id>/update', views.show_update, name='show_update'),                              # Add a New Book Page
    path('show/<int:id>/delete', views.show_delete, name='show_delete'),                              # Add a New Book Page
]