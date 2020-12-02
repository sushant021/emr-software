from django import forms
from django.forms import ModelForm
from .models import Patient, Appointment, Employee, Department
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'username-field', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'password-field', 'placeholder': 'Password'}))


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentForm(ModelForm):
    # class Media:
    #     js = ('confirms.js',)
    class Meta:
        model = Department
        fields = '__all__'


class AppointmentForm(ModelForm):
    date_time = forms.DateTimeField(
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )

    class Meta:
        model = Appointment
        fields = ['id', 'visitor_name', 'description', 'date_time', ]
