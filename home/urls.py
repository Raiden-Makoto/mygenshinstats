from django.urls import path # type: ignore
from .views import get_stats
from django.views.generic import TemplateView # type: ignore

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('get-stats/', get_stats, name='get_stats'),
]