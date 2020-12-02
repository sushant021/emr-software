from django.urls import path, include
from emr import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),

    # authentication
    #    path('', views.user_login, name='login'),
    #    path('logout/', views.user_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # day
    path('day/<int:id>/', views.view_day, name='view_day'),

    # patient_crud
    path('patients/', views.list_patients, name='list_patients'),
    path('search-patient/', views.search_patients, name='search_patient'),
    path('patient/add/', views.add_patient, name='add_patient'),
    path('patient/<int:id>/', views.view_patient, name='view_patient'),
    path('patient/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('patient/update/<int:id>/', views.update_patient, name='update_patient'),

    # appointment_crud
    path('appointments/', views.list_appointments, name='list_appointments'),
    path('appointment/add/', views.add_appointment, name='add_appointment'),
    path('appointment/<int:id>/', views.view_appointment, name='view_appointment'),
    path('appointment/delete/<int:id>/',
         views.delete_appointment, name='delete_appointment'),
    path('appointment/update/<int:id>/',
         views.update_appointment, name='update_appointment'),

    # employee_crud
    path('employees/', views.list_employees, name='list_employees'),
    # path('search-employee/', views.search_employees, name='search_employee'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/<int:id>/', views.view_employee, name='view_employee'),
    path('employee/delete/<int:id>/',
         views.delete_employee, name='delete_employee'),
    path('employee/update/<int:id>/',
         views.update_employee, name='update_employee'),

    # department_crud
    path('departments/', views.list_departments, name='list_departments'),
    # path('search-department/', views.search_departments, name='search_department'),
    path('department/add/', views.add_department, name='add_department'),
    path('department/<int:id>/', views.view_department, name='view_department'),
    path('department/delete/<int:id>/',
         views.delete_department, name='delete_department'),
    path('department/update/<int:id>/',
         views.update_department, name='update_department'),

    # calendar
    path('calendar/', views.calendar, name='calendar')



]
