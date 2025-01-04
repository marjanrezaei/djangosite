from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    path('', index, name = 'index'),
    path('<int:pid>', single, name = 'single'),
    path('category/<str:cat_name>', index, name = 'category'),
    path('tag/<str:tag_name>', index, name = 'tag'),
    path('author/<str:author_username>', index, name = 'author'),
    path('search/', search, name = 'search'),
    path("rss/feed/", LatestEntriesFeed()),
    
]