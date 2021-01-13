from django.core import checks
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.exceptions import PermissionDenied
# from django.contrib.postgres.operations import UnaccentExtension
from django.db.models import * # F, Lookup, Field, Transform, IntegerField, FloatField, Transform, CharField, TextField
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
import warnings
from datetime import timedelta
from django.core.signing import TimestampSigner
import pytz
import re
import itertools
# import foobar


from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.core.files.storage import Storage

from django.contrib.auth.handlers.modwsgi import check_password

from django.core.handlers.wsgi import WSGIHandler


from django.template import Context
from asgiref.sync import sync_to_async
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.core.management.base import BaseCommand, CommandError, no_translations

# import the logging library
import logging
import django
from django.core.signals import request_finished
import django.dispatch
from django.core.checks import Error, register, Tags

# Paginations
from django.core.paginator import Paginator

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

from django.views.generic import ListView


from django.core.cache import CacheKeyWarning
from django.core.cache.backends.locmem import LocMemCache
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.cache import patch_cache_control
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
from django.views.decorators.http import condition
from django.core.signing import Signer

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.postgres.aggregates import BoolAnd
from django.contrib.postgres.aggregates import BoolOr
# from django.contrib.postgres.consints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField, RangeOperators
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from home.models import Contact #, MovieView
from blog.models import Post
from django.contrib import messages

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# from .models import Profile
# from .forms import ProfileModelForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views import View
from django.urls import reverse
# from .utils import token_generator
from django.utils import translation
from django.utils.translation import gettext as _
from django.conf import settings

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.contrib.sites.shortcuts import get_current_site
import threading
from pytube import YouTube
from pytube import Playlist
import os

def movie(request, *args):
	return render(request, 'movie/lol.html')


def detail(request, *args, **kwargs):
	return HttpResponse('Detail Movie Page')		