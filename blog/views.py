from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog\\blog-home.html') 

def single(request):
    context = {'title':'its a title from marjan', 'content':'i try to write a new pasage for example its very fantastic that i can.', 'author':'Marjan Rezayi'}
    return render(request, 'blog\\blog-single.html', context)