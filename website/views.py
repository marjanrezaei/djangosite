from django.shortcuts import render,HttpResponse
from website.models import Contact
from website.forms import NameForm,ContactForm

def index(request):
    return render(request, 'website\index.html') 

def about(request):
    return render(request, 'website\\about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm() 
    return render(request, 'website\contact.html', {'form': form})



def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('valid')
        else:
            return HttpResponse('not valid')

    form = ContactForm()   
    
    return render(request, 'test.html', {'form': form})