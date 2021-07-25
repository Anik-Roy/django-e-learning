"""E_LEARNING URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from E_LEARNING import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('articles/', include('App_Article.urls')),
    path('questions-list/', include('App_QuestionAnswer.urls')),
    path('quiz/', include('App_Quiz.urls')),
    path('', views.home, name='home'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path(r'^ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path(r'^ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

