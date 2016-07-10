from django.contrib import admin
from posts.models import Post
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display =["title","timestamp","updated"]
    list_filter=["timestamp","updated"]
    search_field=["title","content"]
    class Meta:
        model=Post

admin.site.register(Post, PostModelAdmin)
