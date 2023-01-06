from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Apartment, Photo, Contact, Messenger


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'title_description', 'get_photo', 'get_html_photo')

    search_fields = ('address', 'price', 'title_description')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.image.url}' height=200 width=200")

    def get_photo(self, object):
        if object.photo:
            return f"{object.photo.image.url}"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'messenger')

    search_fields = ('phone_number', 'messenger')


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('name_messenger', 'link_messenger')

    search_fields = ('name_messenger', 'link_messenger')