from django.shortcuts import render, redirect
from fav_books_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    # see if the username provided exists in the database
    user = Users.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = logged_user.id
            messages.success(request, "You have Successfully logged in")
            return redirect('/success')
        else:
            # if we didn't find anything in the database by searching by username or if the passwords don't match,
            messages.error(request, "Email or Password incorrect")
            return redirect('/')
    else:
        # if we didn't find anything in the database by searching by username or if the passwords don't match,
        messages.error(request, "Email or Password incorrect")
        return redirect('/')

# : This will clear the massages from messages (error / success) --> redirect to /success
def success_redirect(request):
    list(messages.get_messages(request))
    return redirect('/success')

# : The main page after the user successfully logged in, it will open "The Wall"

def success(request):
    user = Users.objects.get(id=request.session['user_id'])
    msg_objects = Message.objects.all().order_by("-created_at")
    comment_objects = Comment.objects.all().order_by("-created_at")
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'msg_objects': msg_objects,
        'comment_objects': comment_objects,

    }
    return render(request, 'success.html', context)


def reg_process(request):
    # Validation Part Is here
    error = Users.objects.validate(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        return redirect('/')
    else:  # if Validation passed store the user in the db and encrypt the password
        password = request.POST['password']
        ps_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        Users.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=ps_hash
        )
        messages.success(request, "User has been created Successfully!")
        return redirect('/')

# Logout : will terminate the sessions and redirect to the root.


def logout(request):
    # This will clear the massages from messages (error / success)
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')

#  Message Processing: Process the comment : It will take the message and store it in the (message) table at db -- > redirect to /success


def msg_process(request):
    msg = request.POST['msg']
    user = Users.objects.get(id=request.session['user_id'])
    # Validation part for the massages will be added here at the future
    Message.objects.create(message=msg, user=user)
    # to remove the massages.error/success
    list(messages.get_messages(request))
    return redirect('/success')

# Comment Processing: Process the comment : It will take the comment and store it in the (Comment) table at db -- > redirect to /success


def comment_process(request):
    comment = request.POST['comment']
    user = Users.objects.get(id=request.session['user_id'])
    massage = Message.objects.get(id=request.POST['msg_id'])
    # Validation part for the comments will be added here at the future
    # to remove the massages.error/success
    list(messages.get_messages(request))
    # Created a new comment in the db
    Comment.objects.create(comment=comment, user=user, massage=massage)
    return redirect('/success')

# Webpage->|Books| : Open Books
def books_page(request):
    user = Users.objects.get(id=request.session['user_id'])
    books = Book.objects.all()
    tag = check_fav_users(user.id, books)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'user': user,
        'books': books,
        'tag': tag
    }
    return render(request, 'books.html', context)

# Add New Book : This will add new book to the db (Validation included)


def book_process_add(request):
    title = request.POST['title']
    desc = request.POST['desc']
    user_id = request.session['user_id']
    # Validation part
    errors = Book.objects.book_validation(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

    else:
        Book.objects.create(title=title, desc=desc,
                            uploaded_by=Users.objects.get(id=user_id))

    return redirect('/books')

# Webpage -> |Book Details| : Open selected book page and present the book details
# : If the user is the owner of the book they can edit it


def book_details(request, id):
    user = Users.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'user': user,
    }
    return render(request, 'book_details.html', context)

# Process -> : Edit the details of the selected book by the created user.

def book_process_edit(request, id):
    book_id = id
    # Validation Part
    errors = Book.objects.book_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        book_title = request.POST['title']
        book_desc = request.POST['desc']
        book = Book.objects.get(id=book_id)
        book.title = book_title
        book.desc = book_desc
        book.save()
        messages.success(request, "Book Has been successfully edited")
    return redirect('/book_details/' + str(book_id))

# Process -> Add Book to Fav List : Add the selected book to the user in session to his/her favorite books.
def add_to_fav(request, user_id, book_id):
    user = Users.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)

    book.liked_by.add(user)
    return redirect('/books')

''' Process -> Purpose: return a dictionary contains all fav status of the books (if the user have the book at their fav list or not)
# : The dictionary structured as following:
# : dictionary = {
    'book id' : 'favorite status'
    }

    book id : is a variable Key, which represent the related book fav status to session user. 
    favorite status : is the favorite status related to the session user

An example :
    dic = {
    '1' : 'f"<a href='/add_to_fav/{user_id}/{book.id}'> Add to Favorite </a>"' // The user do not have this book as fav in their list
    '2' : '"<p> You already liked this book!<p>"'                              // The user have this book as fav in their list
    '3' : '"<p> You already liked this book!<p>"'                              // The user have this book as fav in their list
    
    }
    '''
def check_fav_users(user_id, books):
    dic = {}

    for book in books:

        # if the query set is empty then 'Add to Favorite'
        if not book.liked_by.all().exists(): 
            dic[f'{book.id}'] = f"<a href='/add_to_fav/{user_id}/{book.id}'> Add to Favorite </a>"
            continue
        for user in book.liked_by.all():
            # If the user already liked this book then 'You Already Liked this Book !' and break the loop
            if (user.id == user_id):
                dic[f'{book.id}'] = "<p> You already liked this book!<p>"
                break 
            # if the program reached this level then this mean user didn't have the book at their favorite list then 'Add to Favorite'
            dic[f'{book.id}'] = f"<a href='/add_to_fav/{user_id}/{book.id}'> Add to Favorite </a>" 

    return dic

# Process -> Remove Book From Fav List: Add the selected book to the user in session to his/her favorite books.
def unfav(request, book_id, user_id):
    book = Book.objects.get(id=book_id)
    user = Users.objects.get(id=user_id)
    book.liked_by.remove(user)
    return redirect(f'/book_details/{book_id}')

# Process -> Delete Book: Add the selected book to the user in session to his/her favorite books.
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')
