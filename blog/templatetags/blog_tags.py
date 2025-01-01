from django import template 
from blog.models import Post, Category, Comment

register = template.Library()

# @register.simple_tag(name='countposts')
# def function_test():
#     post = Post.objects.filter(status=1).count()
#     return post

@register.simple_tag(name='showposts')
def test_show():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=True).count()

@register.filter
def snippet(value,arg=10):
    return value[:arg] + '...'

@register.inclusion_tag('blog//blog-popular-post.html')
def latestposts(arg=2):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}

@register.simple_tag(name='newposts')
def newposts(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return posts

@register.inclusion_tag('blog//blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}



