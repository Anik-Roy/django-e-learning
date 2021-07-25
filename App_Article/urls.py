from django.urls import path
from App_Article import views

app_name = 'App_Article'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('article-detail/<pk>/', views.ArticleDetail.as_view(), name='article_detail'),
    path('edit-article/<pk>/', views.EditArticle.as_view(), name='edit_article'),
    path('delete-article/<pk>/', views.DeleteArticle.as_view(), name='delete_article'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/', views.edit_category, name='edit_category'),
    path('delete-category/', views.delete_category, name='delete_category'),
    path('add-article/', views.AddArticle.as_view(), name='add_article'),
    path('like-article/<pk>/', views.like, name='like_article'),
    path('unlike-article/<pk>/', views.unlike, name='unlike_article'),
    path('edit-comment/<pk>/', views.edit_comment, name='edit_comment'),
    path('delete-comment/<pk>/', views.delete_comment, name='delete_comment'),
]
