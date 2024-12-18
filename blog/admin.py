from django.contrib import admin
from blog.models import Post

# Register your models here.
# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display =('title', 'status', 'published_date', 'content_view')
    empty_value_dispaly = '-empty-'
    # fields = ('title',)
    # exclude = ('title',)
    list_filter = ('status',)
    ordering = ('-published_date',)
    search_fields = ('title', 'content')



admin.site.register(Post, PostAdmin)

