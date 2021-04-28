from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

from .mixins import BaseModelMixin


class User(BaseModelMixin, AbstractUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.username}'

    REQUIRED_FIELDS = ['email', 'first_name']  # Terminal only

    # overrides
    username = models.CharField(
        _('Username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits '
            'and ./_ only.'),
        validators=[MinLengthValidator(
            4,
            message=_('This username is too short. (4 characters minimum)'))],
        error_messages={
            'unique': _("This username is taken."),
            'min_length': _('This username is too short. (4 characters minimum)'),
        },
    )
    first_name = models.CharField(
        _('First name'), max_length=100,
        validators=[MinLengthValidator(2, message=_('Enter your first name.'))])
    last_name = models.CharField(
        _('Last name'), max_length=100,
        validators=[MinLengthValidator(2, message=_('Enter your last name.'))])

    img = models.OneToOneField(
        'miq.Image',
        verbose_name=_('Profile picture'),
        related_name='profile_pic',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
