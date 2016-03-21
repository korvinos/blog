# coding utf-8
from django.contrib import admin
from models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'tags')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

# Register your models here.
