from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.http import JsonResponse
from django.conf.urls.static import static

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #  This is data we want to share with react
        context['sharedData'] = {'message': 'Welcome to my awesome website.'}
        return context


def firstname(request):
    return JsonResponse({'first_name': 'Michaël'})


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/firstname/', firstname, name='firstname'),
    path('', IndexView.as_view(), name='index')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
