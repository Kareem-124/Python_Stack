from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'books': book.objects.all()
    }
    return render(request, 'index.html', context)

# This method is responsible of checking whether the user is trying to add
# a new book or a new author to the Data Base


def process(request):
    if request.POST['process'] == 'create_book':
        book.objects.create(
            title=request.POST['book_title'], desc=request.POST['desc'])
    elif request.POST['process'] == 'create_author':
        author.objects.create(first_name=request.POST['author_first_name'],
                            last_name=request.POST['author_last_name'], notes=request.POST['notes'])
        return redirect('/create_author/')
    return redirect('/')

# Open the Details Page of the Specified Book using its ID


def book_details(request, id):
    id_list = []
    given_book = book.objects.get(id=id)
    given_book_authors = given_book.authors.all()
    # filter out the already existed authors and get the remaining
    rest_authors = author.objects.exclude(
        id__in=[o.id for o in given_book_authors])
    context = {
        'book': given_book,
        'rest_authors': rest_authors
    }
    return render(request, 'book_details.html', context)

# Add Author to a Book (Author --> Book)


def add_author(request):
    author_id = request.POST['author_list']                 # Get Author ID
    book_id = request.POST['book_id']                       # Get Book ID
    # Select the Book record (Book object)  using Book ID
    book_selected = book.objects.get(id=book_id)
    # Select the Author record (Author object) using Author ID
    author_selected = author.objects.get(id=author_id)
    # Add the selected Author record to the Selected Book
    book_selected.authors.add(author_selected)
    # redirect to the same page to refresh the page
    return redirect(f'/book_details/{book_id}')


def create_author(request):
    context = {
        'authors': author.objects.all()
    }
    return render(request, 'author_create.html', context)


def add_book(request):
    author_id = request.POST['author_id']                   # Get Author ID
    book_id = request.POST['book_list']                     # Get Book ID
    # Select the Book record (Book object)  using Book ID
    book_selected = book.objects.get(id=book_id)
    # Select the Author record (Author object) using Author ID
    author_selected = author.objects.get(id=author_id)
    # Add the selected Book record to the Selected Author
    book_selected.authors.add(author_selected)
    # redirect to the same page to refresh the page
    return redirect(f'/author_details/{author_id}')


def author_details(request, id):
    id_list = []
    given_author = author.objects.get(id=id)
    given_author_books = given_author.books.all()
    # filter out the already existed Books and get the remaining
    rest_books = book.objects.exclude(
        id__in=[o.id for o in given_author_books])
    context = {
        'author': given_author,
        'rest_books': rest_books
    }
    return render(request, 'author_details.html', context)
