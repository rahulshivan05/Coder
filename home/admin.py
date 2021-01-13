from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contact, Profile
# Register your models here.

admin.site.register(Contact)
admin.site.register(Profile)

