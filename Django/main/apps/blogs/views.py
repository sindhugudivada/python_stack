from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/')
def show(request,number):
    print number
    return HttpResponse("placeholder to display blog {}".format(number))
def edit(request,number):
    print number
    return HttpResponse("placeholder to edit blog {}".format(number))
def destroy(request,number):
    return redirect('/')
