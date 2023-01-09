from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Apartment, Photo, Contact, Messenger, PhotoApartment


class PhotoApartmentInline(admin.TabularInline):
    model = PhotoApartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = (PhotoApartmentInline,)

    list_display = ('address', 'price', 'title_description', 'get_photo', 'get_first_photo')

    search_fields = ('address', 'price', 'title_description', 'get_photo', 'get_first_photo')

    def get_first_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.first().image.url}' height=200 width=200")

    def get_photo(self, object):
        if object.photo:
            link_photos = []
            for photo in object.photo.all():
                link_photos.append(f"{photo.image.url}")
            return link_photos


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'location', 'description')

    search_fields = ('phone_number', 'location', 'description')


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('name_messenger', 'link_messenger')

    search_fields = ('name_messenger', 'link_messenger')