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
            messages.success(request,"You have Successfully logged in")
            return redirect('/success')
        else:
            # if we didn't find anything in the database by searching by username or if the passwords don't match, 
            messages.error(request,"Email or Password incorrect")
            return redirect('/')
    else:
        # if we didn't find anything in the database by searching by username or if the passwords don't match, 
        messages.error(request,"Email or Password incorrect")
        return redirect('/')
    
def success_redirect(request):
    list(messages.get_messages(request)) 
    return redirect('/success')

def success(request):
    user = Users.objects.get(id = request.session['user_id'])
    msg_objects = Message.objects.all().order_by("-created_at")
    comment_objects = Comment.objects.all().order_by("-created_at")
    context ={
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'msg_objects' : msg_objects,
        'comment_objects' : comment_objects,

    }
    return render(request, 'success.html', context)

def reg_process(request):
    # Validation Part Is here
    error = Users.objects.validate(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password = request.POST['password']
        ps_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        Users.objects.create(
            first_name = request.POST['first_name']
            ,last_name = request.POST['last_name']
            ,email = request.POST['email']
            ,password = ps_hash
        )
        messages.success(request,"User has been created Successfully!")
        return redirect ('/')

def logout(request):
    list(messages.get_messages(request))
    request.session.flush()
    return redirect('/')

def msg_process(request):
    msg = request.POST['msg']
    user = Users.objects.get(id = request.session['user_id'])
    # Validation part for the massages will be added here at the future
    Message.objects.create(message = msg, user = user )
    list(messages.get_messages(request)) # to remove the massages.error/success
    return redirect('/success')

def comment_process(request):
    comment = request.POST['comment']
    user = Users.objects.get(id = request.session['user_id'])
    massage = Message.objects.get(id = request.POST['msg_id'])
    # Validation part for the comments will be added here at the future
    list(messages.get_messages(request)) # to remove the massages.error/success
    Comment.objects.create(comment = comment, user = user , massage = massage) # Created a new comment in the db
    return redirect('/success')

def books_page(request):
    user = Users.objects.get(id = request.session['user_id'])
    books = Book.objects.all()
    tag = check_fav_users(user.id , books )
    print(f"tag = {tag}")
    context ={
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'user': user,
        'books' : books,
        'tag' : tag
    }
    return render(request,'books.html', context)

def book_process_add(request):
    title = request.POST['title']
    desc = request.POST['desc']
    user_id = request.session['user_id']
    # Validation part
    errors = Book.objects.book_validation(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
    
    else:
        Book.objects.create(title = title , desc = desc , uploaded_by = Users.objects.get(id = user_id))
        
    return redirect('/books')

def book_details(request, id):
    user = Users.objects.get(id = request.session['user_id'])
    book = Book.objects.get(id = id)
    context = {
        'book' : book,
        'user' : user,
    }
    return render(request,'book_details.html',context)

def book_process_edit(request,id):
    book_id = id
    # Validation Part
    errors = Book.objects.book_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        book_title = request.POST['title']
        book_desc= request.POST['desc']
        book = Book.objects.get(id = book_id)
        book.title = book_title
        book.desc = book_desc
        book.save()
        messages.success(request,"Book Has been successfully edited")
    return redirect ('/book_details/'+ str(book_id) )

def add_to_fav(request,user_id,book_id):
    user = Users.objects.get(id = user_id)
    book = Book.objects.get(id = book_id)

    book.liked_by.add(user)
    return redirect('/books')

def check_fav_users(user_id, books ):
    dic = {}
    
    for book in books:
        book_found = False
        print(book.liked_by.all())
        if not book.liked_by.all().exists():
            dic[f'{book.id}'] = f"<a href='/add_to_fav/{user_id}/{book.id}'> Add to Favorite </a>"
            continue
        for user in book.liked_by.all():
            # If the user like this book
            if (user.id == user_id) and book_found == False: 
                dic[f'{book.id}'] = "<p> You already liked this book!<p>"
                book_found = True
                break
            dic[f'{book.id}'] = f"<a href='/add_to_fav/{user_id}/{book.id}'> Add to Favorite </a>"
    print(dic)
    return dic

def unfav(request, book_id, user_id):
    book = Book.objects.get(id = book_id)
    user = Users.objects.get(id = user_id)
    book.liked_by.remove(user)
    return redirect (f'/book_details/{book_id}')

def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect ('/books')