from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name = 'index'),
    path('<int:pid>', single, name = 'single'),
    path('category/<str:cat_name>', index, name = 'category'),
    path('author/<str:author_username>', index, name = 'author'),
    path('test', test, name='test'),
]