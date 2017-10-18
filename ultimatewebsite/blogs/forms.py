from django import forms
from blogs.models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'main_image', 'text')


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)