"""project_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import *
from .tasks import *  # Keep it to make Moonsheep aware of defined tasks in DEVELOPMENT_MODE
from .admin import site

urlpatterns = [
    path('admin/', site.urls),
    path('moonsheep/', include('moonsheep.urls')),

    path('', HomeView.as_view(), name='home'),
    path('intro/', TaskIntroView.as_view(), name='task_intro'),
    path('task/', TaskView.as_view(), name='task'),
]

# DEV-DEBUG
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
