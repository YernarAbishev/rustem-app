from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Cabinet, Teacher, Subject, Term, Position, Course, GroupStudy, Schedule, Day, Exam
from .forms import NewUserForm
def homePage(request):
    return render(request, "home.html")
def scheduleGroups(request):
    #filter
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData) | Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    #object
    groups = GroupStudy.objects.all()
    schedules = Schedule.objects.all()
    return render(request, "groups.html", {
        'schedules': schedules,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
    })

def lessonByCourse(request, slug):
    #object
    groups = GroupStudy.objects.all()
    schedules = Schedule.objects.all()
    #filter
    course = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        groups = groups.filter(course=course)

    return render(request, "groups.html", {
        'schedules': schedules,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'course': course,
    })

def lessonByTerm(request, slug):
    #object
    groups = GroupStudy.objects.all()
    schedules = Schedule.objects.all()
    #filter
    term = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        term = get_object_or_404(Term, slug=slug)
        groups = groups.filter(term=term)

    return render(request, "groups.html", {
        'schedules': schedules,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'term': term,
    })

def lessonByPosition(request, slug):
    #object
    groups = GroupStudy.objects.all()
    schedules = Schedule.objects.all()
    #filter
    position = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        position = get_object_or_404(Position, slug=slug)
        groups = groups.filter(position=position)

    return render(request, "groups.html", {
        'schedules': schedules,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'position': position,
    })

def scheduleDetail(request, pk):
    group = get_object_or_404(GroupStudy, pk=pk)
    schedules = Schedule.objects.all()
    schedules = schedules.filter(group=group)
    return render(request, "schedule-detail.html", {
        'schedules': schedules,
        'group': group,
    })

def examGroups(request):
    #filter
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    #object
    groups = GroupStudy.objects.all()
    exams = Exam.objects.all()
    return render(request, "exams.html", {
        'exams': exams,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
    })

def examByCourse(request, slug):
    #object
    groups = GroupStudy.objects.all()
    exams = Exam.objects.all()
    #filter
    course = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        groups = groups.filter(course=course)

    return render(request, "exams.html", {
        'exams': exams,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'course': course,
    })

def examByTerm(request, slug):
    #object
    groups = GroupStudy.objects.all()
    exams = Exam.objects.all()
    #filter
    term = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        term = get_object_or_404(Term, slug=slug)
        groups = groups.filter(term=term)

    return render(request, "exams.html", {
        'exams': exams,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'term': term,
    })

def examByPosition(request, slug):
    #object
    groups = GroupStudy.objects.all()
    exams = Exam.objects.all()
    #filter
    position = None
    terms = Term.objects.all()
    positions = Position.objects.all()
    courses = Course.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        groups = GroupStudy.objects.filter(Q(groupName__icontains=searchData))
    else:
        groups = GroupStudy.objects.all()
    if slug:
        position = get_object_or_404(Position, slug=slug)
        groups = groups.filter(position=position)

    return render(request, "exams.html", {
        'exams': exams,
        'groups': groups,
        'terms': terms,
        'positions': positions,
        'courses': courses,
        'position': position,
    })

def examDetail(request, pk):
    group = get_object_or_404(GroupStudy, pk=pk)
    exams = Exam.objects.all()
    exams = exams.filter(group=group)
    return render(request, "exam-detail.html", {
        'exams': exams,
        'group': group,
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Тіркелу сәтті өтті!")
            return redirect("homePage")
        messages.error(request, "Тіркелу барысында қателіктер пайда болды")
    else:
        form = NewUserForm()
    return render(request, "sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Қош келдіңіз, {username}!")
                return redirect("homePage")
            else:
                messages.error(request, "Логин немесе пароль қате.")
        else:
            messages.error(request, "Логин немесе пароль қате.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Сіз платформадан сәтті шықтыңыз.")
    return redirect("homePage")