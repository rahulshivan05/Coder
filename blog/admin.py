from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, BlogComment


# admin.site.register(Post)
admin.site.register(BlogComment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	class Media:
		js = ('tiny.js',)