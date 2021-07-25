from django.db import models
from App_Login.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_categories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_articles')
    title = models.CharField(max_length=100, blank=False, null=False)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_liked_articles')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='total_likes')
    liked_date = models.DateTimeField(auto_now_add=True)


class Unlike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_unliked_articles')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='total_unlikes')
    unliked_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_comments')
    comment = models.TextField(max_length=264, blank=False, null=False)
    reply = models.ForeignKey('Comment', blank=True, null=True, on_delete=models.CASCADE, related_name='replies')
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date', )

    def __str__(self):
        return self.comment
