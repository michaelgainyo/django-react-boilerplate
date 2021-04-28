from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MiqConfig(AppConfig):
    name = 'miq'
    verbose_name = _('Site Manager')
    verbose_name_plural = _('Site Manager')
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass
