from django.conf.urls import url
from . import views           


urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process', views.getinfo),
    url(r'^result', views.display_result)
]  