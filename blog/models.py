from django.db import models

# Create your models here.
class Post(models.Model):
    #author
    #img
    title = models.CharField(max_length=255)
    content = models.TextField()
    #category
    #tag
    content_view = models.BigIntegerField()
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



