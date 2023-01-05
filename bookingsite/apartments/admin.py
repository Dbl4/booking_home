from django.contrib import admin

from .models import Apartment, Photo


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('address', 'price', 'title_description')

    search_fields = ('address', 'price', 'title_description')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)
