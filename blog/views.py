from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def index(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
          posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
          posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts' : posts}
    return render(request, 'blog\\blog-home.html', context) 

def single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post' : post,}
    return render(request, 'blog\\blog-single.html', context)

def test(request):
    return render(request, 'test.html')