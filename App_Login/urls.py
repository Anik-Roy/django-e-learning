from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('student-login/', views.student_login, name='student-login'),
    path('teacher-login/', views.teacher_login, name='teacher-login'),
    path('student-signup/', views.student_signup, name='student-signup'),
    path('teacher-signup/', views.teacher_signup, name='teacher-signup'),
    path('logout/', views.logout_page, name='logout'),
    path('teachers-profile/', views.teacher_profile, name='teacher-profile'),
    path('edit-teacher-profile/', views.edit_teacher_profile, name='edit-teacher-profile'),
    path('students-profile/', views.student_profile, name='student-profile'),
    path('edit-student-profile/', views.edit_student_profile, name='edit-student-profile'),
    path('home/', views.home, name='home'),
]
