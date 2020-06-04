from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='lead', permanent=False), name=None),
    path('lead', views.lead, name = 'lead'),
    path('deal', views.deal, name = 'deal'),
    path('contact', views.contact, name = 'contact'),
    path('company', views.company, name = 'company')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
