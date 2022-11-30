from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy= 'created_date'
    list_display=['title','creator', 'status','counted_views', 'published_date']
    empty_value_display='-empty-'
    list_filter=('status','creator')
    search_fields=['title','content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=['name', 'email', 'subject', 'created_date', 'updated_date']
    list_filter=['post','name']
    search_fields=['name','subject', 'message']
admin.site.register(Comment, CommentAdmin)

admin.site.register(Category)




