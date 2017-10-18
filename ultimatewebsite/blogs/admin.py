from blogs.models import BlogPost, Comment
from django.contrib import admin

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    '''
        Admin View for BlogPost
    '''
    list_display = ('title', 'author', 'slug', 'created_on')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    '''
        Admin View for Comment
    '''
    list_display = ( 'commenter', 'blogpost', 'comment_text', )

admin.site.register(Comment, CommentAdmin)

admin.site.register(BlogPost, BlogPostAdmin)