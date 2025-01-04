from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        msg = f'You are logged in as {request.user.username}'
    else:
        msg = 'You are  not logged in'
    return render(request, 'accounts\login.html', {'msg': msg}) 

# def logout_view(request):
    # return 

def signup_view(request):
    return render(request, 'accounts\signup.html') 


