from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('v1/', views.index),
    path('v2', TemplateView.as_view(template_name='index.html')),
    # path('v3', TemplateView.as_view(template_name='contact.html')),
    path('v4', views.render_page),
    path('v5', views.redirect_view),
    path('v6', views.RedirectPage.as_view()),
    path('v7', views.Redirect.as_view()),
    path('tasklist', views.render_tasks, name='tasks_list'),
    path('add_task', views.add_task, name='add_task'),
    path('contact_us', views.contact, name='contact'),
    path('contact_us_new', views.contact_new),
    path('add_task_new', views.add_task_new),

]
