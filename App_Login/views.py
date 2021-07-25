from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

# Authentication Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Forms and Models
from App_Login.forms import ProfileForm, SignUpForm
from App_Login.models import Profile
from App_Article.models import Article, Category


# Create your views here.


def student_signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            profile = Profile.objects.get(user=user_obj)
            profile.is_student = True
            profile.save()
            messages.success(request, 'Account created successfully!')
            return redirect('App_Login:student-login')
    return render(request, 'App_Login/student_signup.html', context={'form': form})


def student_login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{request.user} have successfully logged in!')
                return redirect('App_Article:home')
    return render(request, 'App_Login/student_login.html', context={'form': form})


def teacher_signup(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.save()
            profile = Profile.objects.get(user=user_obj)
            profile.is_teacher = True
            profile.save()
            messages.success(request, 'Account created successfully!')
            return redirect('App_Login:teacher-login')
    return render(request, 'App_Login/teacher_signup.html', context={'form': form})


def teacher_login(request):
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{request.user} have successfully logged in!')
                return redirect('App_Article:home')
    return render(request, 'App_Login/teacher_login.html', context={'form': form})


@login_required
def logout_page(request):
    logout(request)
    messages.info(request, 'You are successfully logged out!')
    return redirect('App_Article:home')


@login_required
def teacher_profile(request):
    my_articles = Article.objects.filter(user=request.user)
    print(my_articles)
    categories = Category.objects.all()
    return render(request, 'App_Login/teacher_profile.html', context={'my_articles': my_articles, 'categories': categories})


@login_required
def edit_teacher_profile(request):
    profile_obj = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile_obj)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect('App_Login:teacher-profile')
    return render(request, 'App_Login/edit_teacher_profile.html', context={'form': form, 'categories': categories})


@login_required
def student_profile(request):
    categories = Category.objects.all()
    return render(request, 'App_Login/student_profile.html', context={'categories': categories})


@login_required
def edit_student_profile(request):
    profile_obj = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile_obj)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            return redirect('App_Login:student-profile')
    return render(request, 'App_Login/edit_student_profile.html', context={'form': form, 'categories': categories})


def home(request):
    return render(request, 'App_Login/home.html', context={})
