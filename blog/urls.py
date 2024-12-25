from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:pid>', views.single, name = 'single'),
    path('test', views.test, name='test'),
]