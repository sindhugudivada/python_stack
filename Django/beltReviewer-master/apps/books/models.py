from __future__ import unicode_literals
from django.db import models
import bcrypt, re
  #Our new manager!
  #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def login(self, email, password):
      theUser = User.userManager.filter(email = email)
      if bcrypt.hashpw(password.encode(), theUser[0].password.encode()) == theUser[0].password:
        return {'theUser': theUser[0]}
      else:
        return {'errors': "login Unsuccessful"}

    def register(self, first, last, email, password, confirm):
      errors = False
      erLog = {'errors':[]}
      pattern = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+')
      result = pattern.match(email)
      if result == None:
        errors = True
        erLog['errors'].append('Enter a valid email')
      if len(User.userManager.filter(email= email)) > 1:
        errors = True
        erLog['errors'].append('Email already exists')
      if len(email) < 1:
        errors = True
        erLog['errors'].append('Must enter an email address')
      if len(first) < 2:
        errors = True
        erLog['errors'].append('First name is too short')
      if not first.isalpha():
        errors = True
        erLog['errors'].append('First name must only contain characters')
      if len(last) < 2:
        errors = True
        erLog['errors'].append('Last name is too short')
      if not last.isalpha():
        errors = True
        erLog['errors'].append('Last name must only contain characters')
      if len(password) < 8:
        errors = True
        erLog['errors'].append('password is too short')
      if password != confirm:
        errors = True
        erLog['errors'].append('passwords do not match')
      if errors == True:
        return erLog
      else:
        newUser = User.userManager.create(first_name=first, last_name=last, email=email, password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()))
        return {'theUser': newUser}
      return "registered?"
      pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting 
      # the old hidden objects key with a new one with extra properties!!!
    userManager = UserManager()
    def toString(self):
      return self.first_name + " " + self.last_name + " " + self.email + self.password

class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Reviews(models.Model):
    user_id = models.ForeignKey(User)
    book_id = models.ForeignKey(Book)
    review_text = models.CharField(max_length=1000)
    rating = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


