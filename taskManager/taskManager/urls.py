"""
URL configuration for taskManager project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .register_views import register
from . import register_views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('planner/', include('planner.urls')),
    #path('accounts/login', register_views.MyLoginView.as_view(), name='login'),
    #path('accounts/signup', register_views.MySignupView.as_view(), name='account_signup'),
    #path('accounts/register', register_views.RegisterUser.as_view(), name='register'),
    path('accounts/', include('allauth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.extend(debug_toolbar_urls())