from django.db import models

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .mixins import BaseModelMixin


User = get_user_model()


def upload_to(instance, filename):
    return f'images/{instance.user}/{filename}'


class Image(BaseModelMixin):

    class Meta:
        ordering = ('-updated', '-created',)
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.src.name}'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='images')

    src = models.ImageField(
        verbose_name="Source",
        help_text="Select an image file",
        upload_to=upload_to)

    alt_text = models.CharField(max_length=400, blank=True)
    is_active = models.BooleanField(default=True)
    position = models.PositiveIntegerField(default=0)
