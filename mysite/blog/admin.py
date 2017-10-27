from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish','status')#定义要显示的栏目
    list_filter = ('status', 'created', 'publish', 'author')#定义多个查询功能
    search_fields = ('title', 'body')#定义一个搜索框，从title和body的内容中进行搜索
    prepopulated_fields = {'slug': ('title',)}#将title中的内容预填充到slug中
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(Post,PostAdmin)