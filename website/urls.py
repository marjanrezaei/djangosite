from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('test/', test_view, name='test'),
    path('newsletter/', newsletter_view, name='newsletter'),
    

]