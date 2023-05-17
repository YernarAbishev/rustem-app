from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('user/sign-up/', views.signUp, name='signUp'),
    path('user/login/', views.loginPage, name='loginPage'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
    # lesson
    path('schedule/lessons/group/', views.scheduleGroups, name='scheduleGroups'),
    path('schedule/lessons/group/filter/by-course/<slug:slug>/', views.lessonByCourse, name='lessonByCourse'),
    path('schedule/lessons/group/filter/by-term/<slug:slug>/', views.lessonByTerm, name='lessonByTerm'),
    path('schedule/lessons/group/filter/by-position/<slug:slug>/', views.lessonByPosition, name='lessonByPosition'),
    path('schedule/lessons/group/filter/by-course/<slug:slug>/', views.lessonByCourse, name='lessonByCourse'),
    path('schedule/lessons/group/<int:pk>/', views.scheduleDetail, name='scheduleDetail'),
    # exam
    path('schedule/exams/group/', views.examGroups, name='examGroups'),
    path('schedule/exams/group/filter/by-course/<slug:slug>/', views.examByCourse, name='examByCourse'),
    path('schedule/exams/group/filter/by-term/<slug:slug>/', views.examByTerm, name='examByTerm'),
    path('schedule/exams/group/filter/by-position/<slug:slug>/', views.examByPosition, name='examByPosition'),
    path('schedule/exams/group/filter/by-course/<slug:slug>/', views.examByCourse, name='examByCourse'),
    path('schedule/exams/group/<int:pk>/', views.examDetail, name='examDetail'),

]