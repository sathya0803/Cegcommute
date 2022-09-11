from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User, auth


@login_required(login_url='/login')
def home(request):
    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'volunteer.html')
        else:
            return render(request, 'loginnew.html')
    return render(request, 'loginnew.html')


def signup(request):
    return render(request, 'signup.html')


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return render(request, 'loginnew.html')


@login_required(login_url='/login')
def studentRequest(request):
    if request.method == "POST":
        student1 = Student.objects.all().filter(User1=request.user)
        volunteeruser = User.objects.all().filter(username=request.POST['volunteer'])
        volunteer = Volunteer.objects.all().filter(id=1)
        for i in volunteeruser:
            for j in Volunteer.objects.all().filter(User1=i):
                volunteer = j
        for i in student1:
            StudentRequest.objects.create(
                Student=i,
                StudentArea=i.HomeArea,
                Volunteer=volunteer
            )
        return render(request, 'studentRequest.html')
    return render(request, 'studentRequest.html')


@login_required(login_url='/login')
def student(request):
    if request.method == 'POST':
        context = {}
        area = request.POST['area']
        context['availableVolunteer'] = AvailableVolunteer.objects.all().filter(PickupArea=area)
        return render(request, 'student.html', {'context': context})
    return render(request, 'student.html')


@login_required(login_url='/login')
def companion(request, pk):
    context = {'companion': AvailableVolunteer.objects.all().filter(id=pk)}
    return render(request, 'companions.html', {'context': context})


@login_required(login_url='/login')
def volunteerRequest(request):
    return render(request, 'volunteerRequest.html')


@login_required(login_url='/login')
def volunteer(request):
    if request.method == 'POST':
        print(request.POST)
        AvailableVolunteer.objects.create(
            Volunteer=request.user,
            PickupArea=request.POST['area'],
            Note=request.POST['note']
        )
        return volunteerRequest(request)
    return render(request, 'volunteer.html')
