from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('single', views.single, name = 'single'),
    path('post-<int:pid>', views.test, name='test'),
]