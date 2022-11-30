from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'


class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='blog', default='default.jpg')
    content=models.TextField()
    creator=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=False)
    counted_views=models.IntegerField(default=0)
    # counted_like
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags=TaggableManager()

    class Meta:
        ordering=['-published_date']

    def __str__(self):
        return '{}-{}'.format(self.id, self.title)

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()   
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return self.subject

    

    




