from django.contrib import admin
from App_Article.models import Category, Article, Comment, Like, Unlike

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Unlike)
