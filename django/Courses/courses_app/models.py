from django.db import models

# Create your models here.
class Validate(models.Manager):
    def error_check(self, data):
        errors = {}

        # Validate : name is at least 5 characters
        if len(data['name']) < 5:
            errors['name'] = 'The <strong> Name </strong> Should be at least <strong> 5 </strong> characters'

        # Validate : Description must be at least 15 character
        print(f"Data desc len : {len(data['desc'])}")
        if len(data['desc']) < 15:
            errors['desc'] = "The <strong> Description </strong> must be at least <strong> 15 </strong> characters"

        return errors

class Courses(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validate()


class Comments(models.Model):
    course = models.ForeignKey(Courses,related_name= 'comments', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

