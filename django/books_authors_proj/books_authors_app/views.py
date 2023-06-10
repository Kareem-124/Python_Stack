from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'books' : book.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    if request.POST['process'] == 'create_book':
        book.objects.create(title = request.POST['book_title'] , desc = request.POST['desc'])
    elif request.POST['process'] == 'create_author':
        author.objects.create(first_name = request.POST['author_first_name'] , last_name = request.POST['author_last_name'], notes = request.POST['notes'])
        return redirect('/create_author/')
    return redirect('/')

def book_details(request, id):
    id_list =[]
    given_book = book.objects.get(id = id)
    given_book_authors = given_book.authors.all()
    rest_authors=author.objects.exclude(id__in = [o.id for o in given_book_authors])
    #print(f"The authors of this book are : {given_book_authors}")
    #print(f"The Rest : {rest_authors}")
    context = {
        'book' : given_book,
        'rest_authors': rest_authors
    }
    return render(request, 'book_details.html', context)

def add_author(request):
    author_id = request.POST['author_list']
    book_id = request.POST['book_id']
    book_selected = book.objects.get(id = book_id)
    author_selected = author.objects.get(id = author_id)
    book_selected.authors.add(author_selected)
    return redirect(f'/book_details/{book_id}')

def create_author(request):
    context = {
        'authors' : author.objects.all()
    }
    return render(request, 'author_create.html', context)

def add_book(request):
    author_id = request.POST['author_id']
    book_id = request.POST['book_list']
    book_selected = book.objects.get(id = book_id)
    author_selected = author.objects.get(id = author_id)
    book_selected.authors.add(author_selected)
    return redirect(f'/author_details/{author_id}')

def author_details(request, id):
    id_list =[]
    given_author = author.objects.get(id = id)
    given_author_books = given_author.books.all()
    rest_books=book.objects.exclude(id__in = [o.id for o in given_author_books])
    #print(f"The authors of this book are : {given_book_authors}")
    #print(f"The Rest : {rest_authors}")
    context = {
        'author' : given_author,
        'rest_books': rest_books
    }
    return render(request, 'author_details.html', context)

