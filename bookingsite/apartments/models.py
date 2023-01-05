import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        # Этот параметр указывает Django, что этот класс не является представлением таблицы
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Apartment(TimeStampedMixin, UUIDMixin):
    address = models.CharField(_('address'), max_length=512, blank=True, null=True, default='')
    price = models.IntegerField(_('price'), blank=True, null=True)
    title_description = models.CharField(_('title_description'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('apartment')
        verbose_name_plural = _('apartments')


class Photo(TimeStampedMixin, UUIDMixin):
    image = models.ImageField(_('image'), upload_to='apartment_images', blank=True)

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
