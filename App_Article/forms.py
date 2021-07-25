from django import forms
from App_Article.models import Category, Article, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('created_by', )


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Article
        exclude = ('user', )


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '5', 'placeholder': 'Add a public comment...'}),
                              label='')

    class Meta:
        model = Comment
        fields = ('comment', )
