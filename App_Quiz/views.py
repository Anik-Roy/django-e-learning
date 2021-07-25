from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib import messages
from App_Article.models import Category
from App_Quiz.models import Quiz, QuizQuestion
from App_Quiz.forms import QuizForm, QuizQuestionForm

# Create your views here.


class Home(ListView):
    # form = QuizQuestionForm
    # questions = QuizQuestion.objects.all()
    # for question in questions:
    #     options = {'A': question.option1, 'B': question.option2, 'C': question.option3, 'D': question.option4}
    #     answer = question.answer
    #     print(answer)
    #     print(options[question.answer])
    model = Quiz
    template_name = 'App_Quiz/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CreateQuiz(CreateView):
    model = Quiz
    template_name = 'App_Quiz/add_quiz.html'
    fields = ['title', ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateQuiz, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreateQuiz, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse('App_Quiz:create_quiz_questions', kwargs={'quiz_id': self.object.pk})


def create_quiz_questions(request, quiz_id=None):
    form = QuizQuestionForm(request.user.pk)
    categories = Category.objects.all()
    context = {'categories': categories}

    if quiz_id is not None:
        quiz = Quiz.objects.get(pk=quiz_id)
        form = QuizQuestionForm(request.user.pk, quiz_id)
        context.update({'quiz': quiz})

    if request.method == 'POST':
        form = QuizQuestionForm(request.user.pk, quiz_id, request.POST)

        if form.is_valid():
            quiz_question_obj = form.save(commit=False)

            if quiz_id is not None:
                quiz = Quiz.objects.get(pk=quiz_id)
                quiz_question_obj.quiz = quiz
            else:
                quiz_wrap = form.cleaned_data['quiz_wrap']
                quiz_question_obj.quiz = quiz_wrap

            quiz_question_obj.created_by = request.user
            quiz_question_obj.save()
            messages.success(request, f'Question is saved under quiz " {quiz_question_obj.quiz} "')

        else:
            messages.warning(request, form.errors)
        if quiz_id is not None:
            return HttpResponseRedirect(reverse('App_Quiz:create_quiz_questions', kwargs={'quiz_id': quiz_id}))
        else:
            return HttpResponseRedirect(reverse('App_Quiz:create_quiz_questions'))
    context.update({'form': form})

    return render(request, 'App_Quiz/add_quiz_question.html', context=context)


class ShowQuizQuestions(ListView):
    template_name = 'App_Quiz/show_quiz_questions.html'

    def post(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(pk=self.kwargs['quiz_id'])
        quiz_questions = QuizQuestion.objects.filter(quiz=quiz)
        quiz_answers = {}
        for quiz_question in quiz_questions:
            quiz_answers.update({f'{quiz_question.pk}': quiz_question.answer})

        user_answers = request.POST
        user_answers = dict(user_answers)

        correct = 0
        total_questions = len(quiz_answers)
        user_correct_answer = {}
        user_wrong_answer = {}

        for key, value in user_answers.items():
            if key == 'csrfmiddlewaretoken':
                print('matched')
            else:
                if quiz_answers[key] == value[0]:
                    print(f'correct! your answer -> {value[0]} and correct answer -> ' + quiz_answers[key])
                    correct += 1
                    user_correct_answer.update({key: quiz_answers[key]})
                else:
                    print(f'error! your answer -> {value[0]} and correct answer -> ' + quiz_answers[key])
                    user_wrong_answer.update({key: value[0]})

        print(f'Total question = {total_questions}! Correct answer was -> {correct}')
        request.session['user_correct_answer'] = user_correct_answer
        request.session['user_wrong_answer'] = user_wrong_answer
        request.session['total_correct'] = correct
        request.session['total_marks'] = total_questions

        return HttpResponseRedirect(reverse('App_Quiz:show_quiz_answers', kwargs={'quiz_id': quiz.pk}))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowQuizQuestions, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, pk=self.kwargs['quiz_id'])
        return QuizQuestion.objects.filter(quiz=quiz)


def show_quiz_answers(request, quiz_id):
    user_correct_answer = request.session['user_correct_answer']
    user_wrong_answer = request.session['user_wrong_answer']
    total_correct = request.session['total_correct']
    total_marks = request.session['total_marks']

    # print(user_correct_answer)
    # print(user_wrong_answer)
    categories = Category.objects.all()
    quiz = Quiz.objects.get(pk=quiz_id)
    quiz_questions = QuizQuestion.objects.filter(quiz=quiz)
    return render(request, 'App_Quiz/show_quiz_answers.html', context={'quiz_questions': quiz_questions,
                                                                       'categories': categories,
                                                                       'quiz_id': quiz_id,
                                                                       'total_correct': total_correct,
                                                                       'total_marks': total_marks,
                                                                       'user_correct_answer': user_correct_answer,
                                                                       'user_wrong_answer': user_wrong_answer})
