from django.db import models
import datetime

# Validation Section:
class Validate(models.Manager):
    def new_show_validate(self, Data):
        errors={}
        # Validate : Title has at least 2 characters
        if len(Data['title']) < 2:
            errors['name'] = "Title Should be at least 2 Characters"
        # Validate : The Title is Unique 
        check_title = Show.objects.filter(title = str(Data['title']))
        if check_title.count() > 0:
            errors['title_exists'] = "This Title Already exists"
        # Validate : NetWork has at least 3 characters
        if len(Data['network'])  < 3:
            errors['network'] = "Network should be at least 3 characters"
        # Validate : If user entered a description it has at least 10 characters
        if len(Data['desc']) < 10 and len(Data['desc']) != 0:
            errors['desc'] = "Descriptions Should be at least 10 characters"
        # Try: Get The Date and compare it with the current date
        try:
            # Get Current Date
            date = datetime.datetime.now()
            # Strip The (POST date) we got from the user to prepare it for dates comparison operation
            new_release_date = datetime.datetime.strptime(Data['release_date'], '%Y-%m-%d')
            # If the Current date is smaller than Release Date: add an error massage
            if date < new_release_date:
                errors['release_date'] = "The release date must be in the past"
        # If error ocurred during compiling Then the user didn't enter a release date!
        except:
            errors['release_date'] = "Please enter a release date"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=255)
    desc = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validate()


