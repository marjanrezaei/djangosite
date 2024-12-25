from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', index, name = 'index'),
    path('<int:pid>', single, name = 'single'),
     path('category/<str:cat_name>', blog_category, name = 'category'),
    path('test', test, name='test'),
]