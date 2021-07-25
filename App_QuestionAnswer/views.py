from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_QuestionAnswer.models import Question, Answer
from App_QuestionAnswer.forms import AnswerForm, CommentInAnswerForm
from django.contrib import messages
from App_Article.models import Category
# Create your views here.


class QuestionList(ListView):
    context_object_name = 'questions'
    template_name = 'App_QuestionAnswer/question.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreateQuestion(LoginRequiredMixin, CreateView):
    template_name = 'App_QuestionAnswer/create_question.html'
    model = Question
    fields = ['category', 'title', 'content', ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateQuestion, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateQuestion, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('App_QuestionAnswer:question_detail', kwargs={'pk': self.object.pk})


class QuestionDetail(DetailView):
    template_name = 'App_QuestionAnswer/question_detail.html'
    model = Question
    answer_form = AnswerForm

    def post(self, request, pk):
        if request.method == 'POST':
            if request.user.is_authenticated:
                reply_id = request.POST.get('reply_id')
                if reply_id is not None:
                    comment_in_answer_form = CommentInAnswerForm(request.POST)
                    answer = Answer.objects.get(pk=reply_id)
                    if comment_in_answer_form.is_valid():
                        comment_in_answer_obj = comment_in_answer_form.save(commit=False)
                        comment_in_answer_obj.user = request.user
                        comment_in_answer_obj.answer = answer
                        comment_in_answer_obj.save()
                        messages.success(request, 'Your comment in answer is now public!')
                        return HttpResponseRedirect(reverse('App_QuestionAnswer:question_detail', kwargs={'pk': pk}))
                else:
                    answer_form = AnswerForm(request.POST)
                    question = Question.objects.get(pk=pk)

                    if answer_form.is_valid():
                        answer_obj = answer_form.save(commit=False)
                        answer_obj.question = question
                        answer_obj.user = request.user
                        answer_obj.save()
                        return HttpResponseRedirect(reverse('App_QuestionAnswer:question_detail', kwargs={'pk': pk}))
            else:
                messages.info(request, 'Please login to answer!')
            return HttpResponseRedirect(reverse('App_QuestionAnswer:question_detail', kwargs={'pk': pk}))

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['answer_form'] = self.answer_form
        context['categories'] = Category.objects.all()
        return context


class UpdateQuestion(LoginRequiredMixin, UpdateView):
    pass


class DeleteQuestion(LoginRequiredMixin, DeleteView):
    pass