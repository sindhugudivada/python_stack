from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^home$',views.home),
	url(r'^addBookReview$', views.addBookReview),
	url(r'^createBookReview$', views.createBookReview),
	url(r'^delRev/(?P<id>\d+)$', views.delRev),
	url(r'^showBook/(?P<id>\d+)$', views.showBook),
	url(r'^addReview/(?P<id>\d+)$', views.addReview)
]