from django import template 
from blog.models import Post

register = template.Library()

# @register.simple_tag(name='countposts')
# def function_test():
#     post = Post.objects.filter(status=1).count()
#     return post

@register.simple_tag(name='showposts')
def test_show():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=10):
    return value[:arg] + '...'

@register.inclusion_tag('blog//blog-popular-post.html')
def latestposts(arg=2):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}
