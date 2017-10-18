from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,\
                            HttpResponse
from blogs.forms import BlogPostForm, NewCommentForm
from blogs.models import BlogPost
from django.urls import reverse
# Create your views here.

def blogpost_list(request):
    all_blogpost = BlogPost.objects.all()
    template_name = 'blogs/list.html'
    context = {
        'all_blogpost': all_blogpost
    }
    return render(request, template_name, context)

def blogpost_detail(request, slug):
    all_blogpost = BlogPost.objects.all()
    blogpost = get_object_or_404(BlogPost, slug=slug)

    comments = blogpost.comments.all() # Gathering Comments
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.blogpost = blogpost
            form.commenter = request.user
            form.save()
        return HttpResponseRedirect(reverse('BlogPost Detail', kwargs = {'slug':slug}))
    else:
        form = NewCommentForm()
    context = {
        'blogpost':blogpost, 'all_blogpost':all_blogpost,
        'form':form, 'comments':comments
    }
    return render(request, 'blogs/detail.html', context)








def add_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.author = request.user

            return HttpResponseRedirect(reverse('BlogPost Detail', args = []))
    else:
        form = BlogPostForm()
    return render(request, 'blogs/new_blogpost.html', {'form':form})

def update_blogpost(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance = blogpost)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('BlogPost Detail',
             args = [blogpost.slug]))

    else:
        form = BlogPostForm(instance = blogpost)
    return render(request, 'blogs/new_blogpost.html', {'form':form}).
