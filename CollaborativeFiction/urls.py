"""
URL configuration for CollaborativeFiction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include,re_path


urlpatterns = [
    path("fictions/", include("fictions.urls")),
    path("trustcheck/", include("trustcheck.urls")),
    path("persona/", include("persona.urls")),
    path('comments/', include('django_comments.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),

]

if settings.DEBUG: 
    urlpatterns += [
    re_path(r'^__debug__/', include('debug_toolbar.urls')),
    ]