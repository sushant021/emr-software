from django import template

register = template.Library()


@register.filter(name='appointment_count')
def appointment_count(appointments, user):
    appointments = appointments.filter(user=user)
    return appointments.count()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
