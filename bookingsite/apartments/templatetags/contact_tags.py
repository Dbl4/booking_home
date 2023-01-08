from django import template

from apartments.models import Contact, Messenger


register = template.Library()


@register.simple_tag()
def get_contacts():
    return Contact.objects.all()


@register.simple_tag()
def get_messengers():
    return Messenger.objects.all()