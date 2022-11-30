from django.urls import path
from .views import blog_index, blog_single
from .feeds import LatestEntriesFeed
app_name='blog'
urlpatterns=[
    path('',blog_index,name='index'),
    path('<int:pid>/', blog_single, name='single'),
    path('category/<str:cat_name>',blog_index, name='category'),
    path('tag/<str:tag_name>', blog_index, name='tag'),
    path('search', blog_index, name='search'),
    path('latest/feed/', LatestEntriesFeed()),
]

