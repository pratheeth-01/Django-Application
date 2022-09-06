from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('v1/', views.index, name='index'),
    path('v2', TemplateView.as_view(template_name='index.html')),
    path('v3', TemplateView.as_view(template_name='contact.html')),
    path('v4', views.render_page),

]
