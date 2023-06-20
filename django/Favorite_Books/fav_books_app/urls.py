from django.urls import path     
from . import views

app_name = 'fav_books_app'
urlpatterns = [

    path('', views.index),                                       
    path('success', views.success , name='success'),                                       
    path('success_redirect', views.success_redirect , name='success_redirect'),                                       
    path('reg_process', views.reg_process, name='reg_process'),                                       
    path('login_process', views.login, name='login_process'),                                       
    path('logout_process', views.logout, name='logout_process'),                                       
    path('msg_process', views.msg_process, name='msg_process'),                                       
    path('comment_process', views.comment_process, name='comment_process'),   

    path('books', views.books_page, name='books'),                                    
    path('book_process_add', views.book_process_add, name='book_process_add'),                                    
    path('book_details/<int:id>', views.book_details, name='book_details'),                                
    path('book_process_edit/<int:id>', views.book_process_edit, name='book_process_edit'),                                
    path('add_to_fav/<int:user_id>/<int:book_id>/', views.add_to_fav, name='add_to_fav'),                                
    path('unfav/<int:user_id>/<int:book_id>/', views.unfav, name='unfav'),                                
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),                                


]