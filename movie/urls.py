from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from .views import *
from .import views

urlpatterns = [
    path('', views.movie, name='movie'),
    # path('detail', views.detail, name='detail'),
    # path('<str:slug>', views.blogPost, name='blogPost'),

]