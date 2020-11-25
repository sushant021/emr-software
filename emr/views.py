from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, PatientForm, AppointmentForm, EmployeeForm, DepartmentForm
from .models import Department, Employee, Patient, Appointment, Day
from django.shortcuts import get_object_or_404
from datetime import date
import datetime
from django.utils import timezone


def user_logout(request):
    logout(request)
    return redirect('/')


def search_patients(request):
    message = ''
    error = ''
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        patient_id = request.POST.get('id')
        if len(str(patient_id)) != 0:
            patient = get_object_or_404(Patient, id=patient_id)
            return render(request, 'emr/search_patient.html', {'patient': patient, 'text': 'hello'})
        elif len(patient_name) != 0:
            patients = Patient.objects.filter(full_name__contains=patient_name)
            return render(request, 'emr/search_patient.html', {'patients': patients})
        else:
            message = 'Please provide a patient name or id.'
            return render(request, 'emr/search_patient.html', {'message': message})

        if patient is None:
            error = 'No patient found.'
            return render(request, 'emr/search_patient.html', {'error': error})

    else:
        return render(request, 'emr/search_patient.html')


def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'emr/list_patients.html', {'patients': patients})


def view_patient(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'emr/view_patient.html', {'patient': patient})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patients')
        else:
            error = 'Invalid form submission'
            return render(request, 'emr/add_patient.html', {'form': form, 'error': error})
    else:
        form = PatientForm()
        return render(request, 'emr/add_patient.html', {'form': form})


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('list_patients')


def update_patient(request, id):
    template = 'emr/update_patient.html'
    patient = Patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('list_patients')
    context = {"form": form, 'patient': patient}
    return render(request, template, context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home/')
            else:
                return HttpResponse('Invalid Login Credentials')
        else:
            return HttpResponse('Invalid Form Data')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def home(request):

    today_appointments = []
    day_dates = {}
    upcoming_days = []

    today = date.today()
    today_date = today.strftime("%B %d, %Y")
    appointments = Appointment.objects.all()
    for appointment in appointments:
        appointment_date = appointment.date_time
        appointment_date_formatted = appointment_date.strftime("%B %d, %Y")
        if appointment_date_formatted == today_date:
            today_appointments.append(appointment)

    days = Day.objects.all()
    for day in days:
        day_date = datetime.date(2020, day.month_number, day.number)
        day_dates[day] = day_date

    for day, day_date in day_dates.items():
        if day_date > date.today():
            upcoming_days.append(day)

    template = 'emr/home.html'
    context = {'today_date': today_date,
               'today_appointments': today_appointments, 'upcoming_days': upcoming_days}
    return render(request, template, context)


def view_day(request, id):
    day = Day.objects.get(id=id)
    appointments = day.appointments.all()
    return render(request, 'emr/view_day.html', {'day': day, 'appointments': appointments})


def index(request):
    return HttpResponse('Hello world !')


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
        else:
            error = 'Invalid form submission'
            return render(request, 'emr/add_appointment.html', {'form': form, 'error': error})
    else:
        form = AppointmentForm()
        return render(request, 'emr/add_appointment.html', {'form': form})


def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'emr/list_appointments.html', {'appointments': appointments})


def view_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    template = 'emr/view_appointment.html'
    context = {'appointment': appointment}
    return render(request, template, context)


def delete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('list_appointments')


def update_appointment(request, id):
    template = 'emr/update_appointment.html'
    appointment = Appointment.objects.get(id=id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('list_appointments')
    context = {"form": form, 'appointment': appointment}
    return render(request, template, context)


# employee views

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'emr/list_employees.html', {'employees': employees})


def view_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'emr/view_employee.html', {'employee': employee})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employees')
        else:
            error = 'Invalid form submission'
            return render(request, 'emr/add_employee.html', {'form': form, 'error': error})
    else:
        form = EmployeeForm()
        return render(request, 'emr/add_employee.html', {'form': form})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('list_employees')


def update_employee(request, id):
    template = 'emr/update_employee.html'
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('list_employees')
    context = {"form": form, 'employee': employee}
    return render(request, template, context)


# department views
def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'emr/list_departments.html', {'departments': departments})


def view_department(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'emr/view_department.html', {'department': department})


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_departments')
        else:
            error = 'Invalid form submission'
            return render(request, 'emr/add_department.html', {'form': form, 'error': error})
    else:
        form = DepartmentForm()
        return render(request, 'emr/add_department.html', {'form': form})


def delete_department(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('list_departments')


def update_department(request, id):
    template = 'emr/update_department.html'
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('list_departments')
    context = {"form": form, 'department': department}
    return render(request, template, context)
