from django.conf.urls import url
from RestApp import views

urlpatterns = [
    url(r'^search/$', views.restApi), #if url with search then map it to the restApi method in views class
    url(r'^search/([0-9]+)$', views.restApi)
]
