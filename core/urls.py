from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='lead', permanent=False), name='index'),
    path('lead', views.lead, name = 'lead'),
    path('deal', views.deal, name = 'deal')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
