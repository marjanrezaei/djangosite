from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
          posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    paginator = Paginator(posts, 3)
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
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post' : post,}
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


def test(request):
    return render(request, 'test.html')