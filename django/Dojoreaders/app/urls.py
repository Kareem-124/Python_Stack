from django.urls import path     
from . import views

app_name = 'app'
urlpatterns = [
    # login 'Page'
    path('', views.index),
    # Success 'page'                                        
    path('books', views.success , name='books'),   
    # Success redirect                                    
    path('success_redirect', views.success_redirect , name='success_redirect'),     
    # Registration Process (Validation Included)                                 
    path('reg_process', views.reg_process, name='reg_process'),  
    # Login Process (Validation Included)                                      
    path('login_process', views.login, name='login_process'), 
    # Logout Process                                        
    path('logout_process', views.logout, name='logout_process'), 
    # Delete Book Process                                
    #path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),                                
    ]