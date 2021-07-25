from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View, TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Models & Forms
from App_Article.forms import CategoryForm, ArticleForm, CommentForm
from App_Article.models import Category, Article, Like, Unlike, Comment

# Create your views here.


def home(request):
    return render(request, 'App_Article/home.html', context={})


@login_required
def add_category(request):
    form = CategoryForm
    my_categories = Category.objects.filter(created_by=request.user)
    other_categories = Category.objects.all().exclude(created_by=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(request)
        if form.is_valid():
            category_obj = form.save(commit=False)
            category_obj.created_by = request.user
            category_obj.save()
            form = CategoryForm()
            return HttpResponseRedirect(reverse('App_Article:add_category'))
    return render(request, 'App_Article/add_category.html', context={'form': form, 'my_categories': my_categories,
                                                                     'other_categories': other_categories})


@login_required
def edit_category(request):
    if request.method == 'POST':
        pk = request.POST['articleID']
        category = Category.objects.get(pk=pk)
        print(pk)
        print(category)
        if category is not None:
            form = CategoryForm(request.POST, instance=category)

            if form.is_valid():
                category_name = form.cleaned_data.get('category_name')
                category.category_name = category_name
                category.save()

                messages.success(request, 'Category updated successfully!')
                return HttpResponse('success')
            else:
                errors = form.errors
                return HttpResponse(f'{errors}')
    return HttpResponse('error')


@login_required
def delete_category(request):
    if request.method == 'POST':
        pk = request.POST['articleID']
        category = Category.objects.get(pk=pk)
        category_name = category.category_name
        category.delete()
        messages.success(request, f'Category {category_name} deleted successfully!')
        return HttpResponse('success')
    else:
        return HttpResponse('error')


# def add_article(request):
#     form = ArticleForm
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article_obj = form.save(commit=False)
#             article_obj.user = request.user
#             article_obj.save()
#             return HttpResponseRedirect(reverse('App_Article:home'))
#
#     return render(request, 'App_Article/add_article.html', context={'form': form})


class ArticleList(ListView):
    context_object_name = 'articles'
    paginate_by = 10
    model = Article
    template_name = 'App_Article/article_home.html'

    def get_queryset(self):
        category = self.request.GET.get('query_category')
        if category:
            category = Category.objects.get(category_name=category)
        print(category)
        qs = super(ArticleList, self).get_queryset()
        if category is not None:
            return qs.filter(category=category)
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categories_1'] = Category.objects.all()[:3]
        context['categories_2'] = Category.objects.all()[3:6]
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'App_Article/article_detail.html'

    comment_form = CommentForm

    def post(self, request, pk):
        if request.method == 'POST':
            if request.user.is_authenticated:
                comment_form = CommentForm(request.POST)
                reply_id = None
                article = Article.objects.get(pk=pk)
                if comment_form.is_valid():
                    comment_obj = comment_form.save(commit=False)
                    comment_obj.user = request.user
                    comment_obj.article = article
                    if request.POST.get('reply_id') is not None:
                        reply_id = request.POST.get('reply_id')
                        comment = Comment.objects.get(pk=reply_id)
                        comment_obj.reply = comment
                    comment_obj.save()
                    comment_form = CommentForm
                    if request.POST.get('reply_id') is not None:
                        messages.success(request, 'Your reply is now public!')
                    else:
                        messages.success(request, 'Your comment is now public!')
            else:
                messages.info(request, 'Please login to comment!')
            return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk': article.pk}))

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['categories_1'] = Category.objects.all()[:3]
        context['categories_2'] = Category.objects.all()[3:6]
        likes_obj = Like.objects.filter(article=self.object.pk)
        likes_list = likes_obj.values_list('user', flat=True)

        unlikes_obj = Unlike.objects.filter(article=self.object.pk)
        unlikes_list = unlikes_obj.values_list('user', flat=True)

        context['comment_form'] = self.comment_form
        context['comments'] = Comment.objects.filter(article=self.object.pk, reply=None)
        context['likes_list'] = likes_list
        context['unlikes_lists'] = unlikes_list

        return context


class AddArticle(LoginRequiredMixin, CreateView):
    template_name = 'App_Article/add_article.html'
    model = Article
    fields = ['category', 'title', 'content', 'image', ]
    success_url = f'/articles/article-detail/{model.pk}/'

    def form_valid(self, form):
        print(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddArticle, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('App_Article:article_detail', kwargs={'pk': self.object.pk})


class EditArticle(LoginRequiredMixin, UpdateView):
    template_name = 'App_Article/edit_article.html'
    model = Article
    fields = ['category', 'title', 'content', 'image', ]

    def get_context_data(self, **kwargs):
        context = super(EditArticle, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('App_Article:article_detail', kwargs={'pk': self.object.pk})


class DeleteArticle(LoginRequiredMixin, DeleteView):
    template_name = 'App_Article/delete_article.html'
    model = Article
    success_url = '/account/teachers-profile/'


@login_required
def like(request, pk):
    liked_article = Article.objects.get(pk=pk)
    liker_user = request.user
    already_liked = Like.objects.filter(user=liker_user, article=liked_article)
    already_unliked = Unlike.objects.filter(user=liker_user, article=liked_article)

    if already_unliked:
        already_unliked.delete()

    if not already_liked:
        like_obj = Like(user=request.user, article=liked_article)
        like_obj.save()
    else:
        already_liked.delete()
    return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk': pk}))


@login_required
def unlike(request, pk):
    unliked_article = Article.objects.get(pk=pk)
    unliker_user = request.user
    already_liked = Like.objects.filter(user=unliker_user, article=unliked_article)
    if already_liked:
        already_liked.delete()

    already_unliked = Unlike.objects.filter(user=unliker_user, article=unliked_article)
    if not already_unliked:
        unlike_obj = Unlike(user=unliker_user, article=unliked_article)
        unlike_obj.save()
    else:
        already_unliked.delete()
    return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk': pk}))


@login_required
def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment is updated successfully!')
            return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk': comment.article.pk}))
    return render(request, 'App_Article/edit_comment.html', context={'form': form})


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    article_id = comment.article.pk
    if request.method == 'POST':
        article_id = comment.article.pk
        comment.delete()
        messages.success(request, 'Your comment is deleted!')
        return HttpResponseRedirect(reverse('App_Article:article_detail', kwargs={'pk': article_id}))
    return render(request, 'App_Article/delete_comment.html', context={'pk': pk, 'article_id': article_id})
