import uuid

from django.core.validators import RegexValidator
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
    address = models.CharField(_('address'), max_length=255, blank=True, null=True, default='')
    price = models.IntegerField(_('price'), blank=True, null=True)
    title_description = models.CharField(_('title description'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    photo = models.ManyToManyField('Photo', through='PhotoApartment')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('apartment')
        verbose_name_plural = _('apartments')


class PhotoApartment(UUIDMixin):
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)


class Photo(TimeStampedMixin, UUIDMixin):
    image = models.ImageField(_('image'), upload_to='apartment_images', blank=True)

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')


class Contact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    description = models.TextField(_('description'), blank=True, null=True)
    location = models.TextField(_('location'), blank=True, null=True)
    messenger = models.ForeignKey('Messenger', on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class Messenger(models.Model):
    name_messenger = models.CharField(_('name_messenger'), max_length=255, blank=True, null=True)
    link_messenger = models.CharField(_('link_messanger'), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name_messenger

    class Meta:
        verbose_name = _('messenger')
        verbose_name_plural = _('messengers')
