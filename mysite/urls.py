from django.urls import path
from .views import index, about, contact
from django.contrib.auth import views as auth_views

app_name='mysite'
urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
]