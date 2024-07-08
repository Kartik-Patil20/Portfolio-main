# application/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view-project/', views.view_github_project, name='view_github_project'),
    path('view-certificates/', views.view_certificates, name='view_certificates'),
     
]
