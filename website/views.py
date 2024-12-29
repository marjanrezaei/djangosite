from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm, NewsLetterForm
from django.contrib import messages

def index(request):
    return render(request, 'website\index.html') 

def about(request):
    return render(request, 'website\\about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submitted')
    form = ContactForm() 
    return render(request, 'website\contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


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