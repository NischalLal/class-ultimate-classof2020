from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class CommonDateTimeInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class BlogPost(CommonDateTimeInfo):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    author = models.ForeignKey(User, related_name = 'uploaded_blogpost')
    main_image = models.ImageField(upload_to = 'blogs')
    text = models.TextField()

    class Meta:
        ordering = ('-created_on',)
        verbose_name = 'Blogpost'
        verbose_name_plural = 'Blogposts'

    def __str__(self):
        return self.title