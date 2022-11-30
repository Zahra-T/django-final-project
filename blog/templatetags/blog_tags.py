from django import template
from blog.models import Post, Category, Comment
from taggit.models import Tag
register=template.Library()

@register.inclusion_tag('blog/blog-recent-posts.html')
def recent_posts(number=3):
    return {'posts':Post.objects.filter(status=1).order_by('-published_date')[:number]}

@register.inclusion_tag('blog/blog-categories.html')
def categories():
    categories=Category.objects.all()
    return {'categories':categories}

@register.inclusion_tag('blog/blog-tags.html')
def tags():
    return {'tags':Tag.objects.all()}

@register.inclusion_tag('blog/blog-post.html')
def blog_post(post, truncatechars=None):
    if truncatechars==None:
        return {'post':post, 'content':post.content}
    return {'post':post, 'content':post.content[:truncatechars]+'...'}

@register.simple_tag
def comments_number(id):
    return Comment.objects.filter(post__id=id, approved=1).count()

@register.simple_tag
def popular_posts():
    return Post.objects.filter(status=1).order_by('-counted_views')[:6]



