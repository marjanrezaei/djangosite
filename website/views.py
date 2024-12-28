from django.shortcuts import render
from website.models import Contact

def index(request):
    return render(request, 'website\index.html') 

def about(request):
    return render(request, 'website\\about.html')


def contact(request):
    return render(request, 'website\contact.html')



def test_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        c = Contact()
        c.name = name
        c.subject = subject
        c.email = email
        c.message = message
        c.save()    
    
    return render(request, 'test.html')