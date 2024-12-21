from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1)
    context = {'posts' : posts}
    return render(request, 'blog\\blog-home.html', context) 

def single(request):
    context = {'title':'its a title from marjan', 'content':'i try to write a new pasage for example its very fantastic that i can.', 'author':'Marjan Rezayi'}
    return render(request, 'blog\\blog-single.html', context)


def test(request,pid):
    # post = Post.objects.get(pk=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post' : post,}
    return render(request, 'test.html', context)