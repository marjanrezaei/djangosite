from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

# @login_required  # if login_required
def index(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
          posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    paginator = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = paginator.page(page_number)  
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)
  

    context = {'posts' : posts}
    return render(request, 'blog\\blog-home.html', context) 

def single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submitted')
            
    post = get_object_or_404(Post, pk=pid, status=1)
    comments = Comment.objects.filter(post=post.id, approved=True)
    form = CommentForm()
    context = {'post' : post, 'comments' : comments, 'form' : form}
    return render(request, 'blog\\blog-single.html', context)

def search(request):    
    posts = Post.objects.filter(status=1)
    # print(request.__dict__)
    if request.method == 'GET':
        #  print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts' : posts}
    return render(request, 'blog\\blog-home.html', context) 

