from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book, Author, Reviews
import bcrypt
def index(request):
    return render(request, "books/login.html")

def login(request):
	if request.method == "POST":
		#do this
		#return render(request, "login/success.html")
		answer = User.userManager.login(request.POST.get('email'), request.POST.get('password'))
		if answer.has_key('errors'):
			return HttpResponse(answer['errors'])
		else:
			theUser = answer['theUser']
			request.session['user'] = theUser.first_name
			request.session['id'] = theUser.id
			return redirect('/home')
	else:
		return redirect('/')

def home(request):
	mostRecent = Reviews.objects.all().order_by('-created_at')[:3]
	books = Book.objects.all()
	context = {'reviews': mostRecent, 'books':books}
	return render(request, "books/home.html", context)

def register(request):
	if request.method == "POST":
		#do this
		answer = User.userManager.register(request.POST.get('first'), request.POST.get('last'), request.POST.get('email'), request.POST.get('password'), request.POST.get('confirm'))
		print(answer)
		if answer.has_key('errors'):
			return HttpResponse(answer['errors'])
		else:
			return redirect('/')
	else:
		return redirect('/')

def delRev(request,id):
	review = Reviews.objects.get(id=id)
	review.delete()
	return redirect('/home')

def addBookReview(request):
	authors = Author.objects.all()
	context = {"authors": authors}
	return render(request, "books/add.html", context)

def createBookReview(request):
	if request.method == "POST":
		user = User.userManager.get(id=request.session['id'])
		if request.POST.get('newAuthor') != "":
			newAuth = Author.objects.create(name=request.POST.get('newAuthor'))
			newBook = Book.objects.create(title=request.POST.get('title'), author=newAuth)
			newReview = Reviews.objects.create(user_id=user, book_id=newBook, review_text=request.POST.get('review'), rating=request.POST.get('rating'))
			return redirect('/home')
		else:
			author = Author.objects.get(id=request.POST.get('authors'))
			newBook = Book.objects.create(title=request.POST.get('title'), author=author)
			newReview = Reviews.objects.create(user_id=user, book_id=newBook, review_text=request.POST.get('review'), rating=request.POST.get('rating'))
			return redirect('/home')
	else:
		return redirect('/home')

def showBook(request, id):
	user = User.userManager.get(id=request.session['id'])
	book = Book.objects.get(id=id)
	reviews = Reviews.objects.filter(book_id=book)
	context = {
	"book": book,
	"reviews": reviews
	}
	return render(request, 'books/book.html', context)

def addReview(request,id):
	if request.method =="POST":
		user = User.userManager.get(id=request.session['id'])
		book = Book.objects.get(id=id)
		review = Reviews.objects.create(user_id=user, book_id=book, review_text=request.POST.get('review'), rating=request.POST.get('rating'))
		return redirect('/home')