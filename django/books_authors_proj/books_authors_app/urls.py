from django.urls import path     
from . import views

app_name = 'books_authors_app'
urlpatterns = [
    path('', views.index, name='home_page'),                                        # Add a New Book Page
    path('create_author/', views.create_author, name='create_author'),              # Add a New Author Page
    path('process', views.process, name='process'),                                 # process Book/Author creation
    path('book_details/<int:id>', views.book_details, name='book_details'),         # Open Details Page for a book
    path('add_author/', views.add_author, name='add_author'),                       # Add Author to a Book (Author --> Book)
    path('author_details/<int:id>', views.author_details, name='author_details'),   # Open Details Page for an Author
    path('add_book/', views.add_book, name='add_book'),                             # Add Book to an Author (Book --> Author)

]