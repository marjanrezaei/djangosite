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