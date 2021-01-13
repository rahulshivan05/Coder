"""iCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sitemaps.views import sitemap

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


admin.site.site_header = "iCoder Admin"
admin.site.site_title = "iCoder Admin Panel"
admin.site.index_title = "Welcome to iCoder Admin Panel"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    # path('', include('home.urls')),
    path('accounts/login/', auth_views.LoginView.as_view()),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #  name='django.contrib.sitemaps.views.sitemap')
    
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('home.urls')),
    # path('movie/', include('movie.urls')),
    prefix_default_language = False,
)
