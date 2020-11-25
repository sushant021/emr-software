from django import template

register = template.Library()


@register.filter(name='appointment_count')
def appointment_count(appointments, user):
    appointments = appointments.filter(user=user)
    return appointments.count()
