from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt
my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = []
        if len(self.filter(email=postData['email'])) > 0:
            # check this user's password
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')
        if errors:
            return errors
        return user

    def register_validator(self,postData):
        errors = []
        # check name and last name length
        if len(postData['name']) < 2 or len(postData['alias']) < 2:
            errors.append("User name/alias should be more than 2 characters")
        # check password
        if len(postData['password']) < 8:
            errors.append("Password should have more than 8 characters")    
        #check name for character
        if not re.match(NAME_REGEX, postData['name']) or not re.match(NAME_REGEX, postData['alias']):
            errors.append("User name/last name should contains only letters")
        # check email 
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("Invalid email format")
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use")
        # check password
        if postData['password'] != postData['confirm_password']:
            errors.append("Password doesn't match")
        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
            print "hashed code: ", hashed
            new_user = self.create(
                name=postData['name'],
                alias=postData['alias'],
                email=postData['email'],
                password=hashed
            )
            return new_user
        return errors   

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "User: --{}".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #def __repr__(self):
     #   return "Book: -----{}".format(self.title)
class Review(models.Model):
    comment = models.CharField(max_length=255)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User,related_name="reviews")
    book=models.ForeignKey(Book,related_name="book_reviews")
    def __repr__(self):
        return "Review: ---{}, Rate: ---{}".format(self.comment, self.rating)
   



