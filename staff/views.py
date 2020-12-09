from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Q
from .forms import *
from .models import *
import requests
import json



@login_required(login_url = '/login/')
def addUserProfile(request):
    template_name = "pages/addUserProfile.html"
    context = {}
    profiles = StaffProfile.objects.all()
    units = Unit.objects.all()
    accademicsession = AccademicSession.objects.all()
    context['profiles'] = profiles
    context['units'] = units
    context['accademicsession'] = accademicsession

    user_qs = User.objects.all()
    dept_qs = Department.objects.all()
    unitform = UnitForm()
    sform = AccademicSessionForm()
    context['sform'] = sform
    context['unitform'] = unitform
    context['user_qs'] = user_qs
    context['dept_qs'] = dept_qs

    if request.method == 'POST':
        form = StaffProfileForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_id = request.POST.get('user_id')
            obj.user_level = request.POST.get('user_level')
            obj.department_id = request.POST.get('department_id')
            obj.save()
            messages.success(request, 'User Added Successfully')
            return redirect('/profile/')
        
        else:
            messages.warning(request, 'fill all the fields')
            return redirect('/profile/')
    else:
        form = StaffProfileForm()
        context['form'] = form

    return render(request, template_name, context)
@login_required(login_url = '/login/')
def allReport(request):
    context = {}
    template_name = 'pages/allreport.html'
    reports = Report.objects.all()
    context['reports'] = reports
    return render(request, template_name, context)

@login_required(login_url = '/login/')
def report(request, id):
    context = {}
    report = Report.objects.get(id = id)

    import random

    rand = random.randint(100,2000)
    print(rand)
    context['report'] = report
    context['rand'] = rand
    template_name = 'pages/report.html'
    
    return render(request, template_name, context)



@login_required(login_url = '/login/')
def dashboardView(request):
    context = {}
    profiles = StaffProfile.objects.all()
    units = Unit.objects.all()
    accademicsession = AccademicSession.objects.all()
    context['profiles'] = profiles
    context['units'] = units
    context['accademicsession'] = accademicsession


    unitform = UnitForm()
    sform = AccademicSessionForm()
    context['sform'] = sform
    context['unitform'] = unitform
    reports_qs_count = Report.objects.all().count()
    units_qs_count = Unit.objects.all().count()
    staffs_qs_count = StaffProfile.objects.all().count()
    lect_staff_qs = StaffProfile.objects.filter(user_level='LEC')
    depts_qs_count = Department.objects.all().count()
    context['reports_qs_count'] = reports_qs_count
    context['lect_staff_qs'] = lect_staff_qs
    context['units_qs_count'] = units_qs_count
    context['staffs_qs_count'] = staffs_qs_count
    context['depts_qs_count'] = depts_qs_count
    
    template_name = 'pages/dashboard.html'

    return render(request, template_name, context)

def loginView(request):

    template_name = 'auth/login.html'
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':

        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # str_relace = str.replace(username, '/', f'')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'login was successful')
            return redirect('/dashboard/')
        else:
            messages.warning(request, f'login Error !!!! Provide Correct Username And Password')
            return redirect('/')
    else:
        form = UserLoginForm()

    return render(request, template_name, {'form': form})
@login_required(login_url = '/login/')
def allqs(request):
    template_name = 'pages/all.html'
    context = {}
    lect_staff_qs = StaffProfile.objects.filter(user_level='LEC')
    hod_staff_qs = StaffProfile.objects.filter(user_level='HOD')
    dean_staff_qs = StaffProfile.objects.filter(user_level='DEAN')

    context['lect_staff_qs'] = lect_staff_qs
    context['hod_staff_qs'] = hod_staff_qs
    context['dean_staff_qs'] = dean_staff_qs

    return render(request, template_name, context)


def registerView(request):

    template_name = 'auth/register.html'

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/login/')
        else:
            messages.warning(request, f'Something went wrong please fil in the form correctly')
            form.save()
            return redirect('/registration/')

    else:
        form = UserRegisterForm() 
     
    return render(request, template_name, {'form': form })
@login_required(login_url = '/login/')
def addUnit(request):
    if request.method == 'POST':

        form = UnitForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Adding Unit was successful')
            return redirect('/dashboard/')
        else:
            messages.success(request, f'Adding Unit was Unsuccessful')
            return redirect('/dashboard/')
@login_required(login_url = '/login/')
def allocateWithReport(request):
    if request.method == 'POST':

        rform = ReportForm(request.POST)

        Report.objects.create(
            staffprofile_id = request.POST.get('staffprofile_id'),
            unit_id = request.POST.get('unit_id'),
            accademicsession_id = request.POST.get('accademicsession_id')
        )

        messages.success(request, f'Course Allocation was successful')
        messages.success(request, f'Report Generation also was successful')
        return redirect('/dashboard/')

        # if rform.is_valid():
        #     obj = rform.save(commit=False)
        #     obj.staffprofile = request.POST.get('staffprofile_id')
        #     obj.unit = request.POST.get('unit_id')
        #     obj.accademicsession = request.POST.get('accademicsession_id')

        #     obj.save()
        #     messages.success(request, f'Course Allocation was successful')
        #     messages.success(request, f'Report Generation also was successful')
        #     return redirect('/dashboard/')
        # else:
        #     messages.success(request, f'Course Allocation was Unsuccessful')
        #     return redirect('/dashboard/')


@login_required(login_url = '/login/')
def addSession(request):
    if request.method == 'POST':

        sform = AccademicSessionForm(request.POST)

        if sform.is_valid():
            sform.save()
            messages.success(request, f'AccademicSession add was successful')
            return redirect('/dashboard/')
        else:
            messages.success(request, f'AccademicSession add was Unsuccessful')
            return redirect('/dashboard/')

def loguotView(request): 
    logout(request)  
    messages.success(request, f'You Have logout !!!')
    return redirect('/login/')