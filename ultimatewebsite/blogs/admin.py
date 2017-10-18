from blogs.models import BlogPost
from django.contrib import admin

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    '''
        Admin View for BlogPost
    '''
    list_display = ('title', 'author', 'slug', 'created_on')
    prepopulated_fields = {'slug':('title')}


admin.site.register(BlogPost, BlogPostAdmin)