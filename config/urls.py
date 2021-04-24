from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView  # Our homepage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='base.html'), name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
