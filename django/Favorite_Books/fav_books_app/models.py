from django.db import models
import re


# Create your models here.
class Validation(models.Manager):
    def validate(self, data):
        error = {}

        if len(data['first_name']) < 2 :
            error['firs_name'] = "First Name should be at least 2 characters"
        
        if len(data['last_name']) < 2:
            error['last_name'] = "Last Name should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']):    # test whether a field matches the pattern            
            error['email'] = "Invalid email address!"
        
        if data['password'] != data['conf_password']:
            error['password_conf'] = "Password and Password Confirmation should Match!"
        
        if len(data['password']) < 8 :
            error['password'] = "Password Must be at least 8 characters"
        return error

class Users(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = Validation()
    # messages : a list of Massage instance
    # comments : a list of Comment instance
    # fav_books: a list of fav books (liked) by this user


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(Users,related_name="messages",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # comments : a list of Comment instance


class Comment(models.Model):
    comment = models.TextField()
    massage = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name="comments", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class BookValidation(models.Manager):
    def book_validation(self,data):
        errors = {}
        if len(data['title']) < 1:
            errors['title'] = "You Must Add a Title! "
        
        if len(data['desc']) < 5:
            errors['desc'] = "The Book Description must be at least 5 characters!"
        
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    liked_by = models.ManyToManyField(Users, related_name="fav_books")
    uploaded_by = models.ForeignKey(Users, related_name= "books_uploaded", on_delete=models.CASCADE)
    desc = models.TextField(default="NO Description Available")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BookValidation()



