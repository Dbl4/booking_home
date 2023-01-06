from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Apartment, Photo, Contact, Messenger, PhotoApartment


class PhotoApartmentInline(admin.TabularInline):
    model = PhotoApartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = (PhotoApartmentInline,)

    # list_display = ('address', 'price', 'title_description', 'get_photo', 'get_html_photo')
    list_display = ('address', 'price', 'title_description',)

    search_fields = ('address', 'price', 'title_description')

    # def get_html_photo(self, object):
    #     if object.photo:
    #         yield mark_safe(f"<img src='{object.photo.image.url}' height=200 width=200")
    #
    # def get_photo(self, object):
    #     if object.photo:
    #         yield f"{object.photo.image.url}"


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