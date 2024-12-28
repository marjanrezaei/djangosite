from django.shortcuts import render,HttpResponse
from website.models import Contact
from website.forms import NameForm

def index(request):
    return render(request, 'website\index.html') 

def about(request):
    return render(request, 'website\\about.html')


def contact(request):
    return render(request, 'website\contact.html')



def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, subject, email, message)
            return HttpResponse('valid')
        else:
            return HttpResponse('not valid')

    form = NameForm()   
    
    return render(request, 'test.html', {'form': form})