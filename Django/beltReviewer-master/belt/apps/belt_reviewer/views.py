from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'belt_reviewer/index.html')

def register(request):
    result = User.objects.register_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/books')

def login(request):
    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/books')

def display(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    user=User.objects.get(id=request.session['user_id'])
    context = {
    'user': user,
    'latest': Review.objects.order_by('created_at').reverse()[:3],
    'rest': Review.objects.order_by('created_at').reverse(),
    }
    return render(request, "belt_reviewer/home.html", context)

def add(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, "belt_reviewer/new.html", context)

def addBook(request):
    print request.session['user_id']
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.create(
        title = request.POST['title'],
        author = request.POST['author']
        
    )
    review = Review.objects.create(
        comment = request.POST['comment'],
        rating = request.POST['stars'],
        reviewer = user,
        book = book
    )
    context = {
        "user" : user,
        "bookCreated" : book,
        "reviewCreated" : review,  
    }
    url = "/title/" + str(book.id)
    return redirect(url)

def addReview(request,book_id):
   
    print book_id
    review = Review.objects.create(
        comment = request.POST['comment'],
        rating = request.POST['stars'] ,
        book=Book.objects.get(id=book_id),
        reviewer=User.objects.get(id=request.session['user_id'])
    )
    context = {
        "reviewCreated" : review
    }
    url = "/title/" + str(book.id)
    return redirect(url)


def showBook(request, book_id):
    bookToShow = Book.objects.get(id=book_id)
    context = {
        'book': bookToShow,
        'all_reviews': bookToShow.book_reviews.all()
    }
    return render(request, 'belt_reviewer/review.html', context)

def userpage(request, id):
    user = User.objects.get(id=id)
    review = Review.objects.filter(reviewer=user)
    count = review.count()
    print count
    context = {
        "user" : user,
        "reviewedBooks" : review,
        "countReviews": count
    }
    return render(request,'belt_reviewer/user.html', context)

def destroy(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.session['user_id'] == review.reviewer.id:
        review.delete()
    return render(request, "belt_reviewer/review.html")


def logout(request):
    context = {
        "logout" : request.session.pop("user_id")
        }
    return render(request, "belt_reviewer/index.html", context)

