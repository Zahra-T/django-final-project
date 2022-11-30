from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .models import Post, Comment
from django.core.paginator import Paginator
from blog.forms import CommentForm
from django.urls import reverse
from django.contrib import messages

def blog_index(request, **kwargs):
    posts=Post.objects.filter(published_date__lte=timezone.now())
    Post.objects.filter(published_date__gt=timezone.now(), status=0).update(status=1)
    if kwargs.get('cat_name'):
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
    if param := request.GET.get('q'):
        posts = posts.filter(Q(title__contains=param) | Q(content__contains=param))
    pages = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = pages.get_page(page_number)
    context={'posts':posts}
    return render(request, 'blog/blog-index.html',context)

def blog_single(request, pid):
    post=get_object_or_404(Post, status=1, pk=pid)
    if request.method=='POST':
        form=CommentForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment successfully submited.')
        else:
            messages.add_message(request, messages.ERROR, 'Sorry, someting went wrong. your comment didn\'t submit')
        return redirect(reverse('blog:single', kwargs={'pid':post.id}))
    comments=Comment.objects.filter(post__id=pid, approved=True)
    post.counted_views+=1
    post.save()
    context={'post':post, 'comments':comments}
    return render(request, 'blog/blog-single.html', context)
