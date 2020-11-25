from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_department', args=[self.id])


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=254)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees')
    designation = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(auto_now_add=True, blank=True)
    address = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    contact_number = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('view_employee', args=[self.id])


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    full_name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True)
    contact = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(blank=True)
    medical_history = models.TextField(blank=True)
    initial_diagnosis = models.TextField(blank=True)
    updated_diagnosis = models.TextField(blank=True)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('view_patient', args=[self.id])


class Day(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    month = models.CharField(max_length=20)
    month_number = models.IntegerField()
    week_day = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        date = str(self.month) + ' ' + str(self.number)
        return date

    def get_absolute_url(self):
        return reverse('view_day', args=[self.id])


class Appointment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='appointments', default=1)
    id = models.AutoField(primary_key=True)
    visitor_name = models.CharField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    date_time = models.DateTimeField(default=timezone.now)
    day = models.ForeignKey(Day, on_delete=models.CASCADE,
                            related_name='appointments', blank=True)

    class Meta:
        ordering = ('date_time',)

    def save(self, *args, **kwargs):
        appointment_day_month = str(self.date_time.strftime("%B"))
        appointment_day_number = self.date_time.strftime("%d")
        appointment_day = Day.objects.get(
            month=appointment_day_month, number=appointment_day_number)
        self.day = appointment_day
        super(Appointment, self).save(*args, **kwargs)

    def __str__(self):
        return self.visitor_name

    def get_absolute_url(self):
        return reverse('view_appointment', args=[self.id])
