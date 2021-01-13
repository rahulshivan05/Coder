from django.db import models

from django.db.models import Func, Q
from django.contrib.postgres.fields import HStoreField
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.contrib.postgres.fields import IntegerRangeField
from .utils import get_random_code
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password


import logging
import traceback

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
import ipinfo
from simple_history.models import HistoricalRecords


LOGGER = logging.getLogger(__name__)


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=75)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return 'Message from ' + self.name


# class MovieView(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=1000)
#     image = models.ImageField(upload_to='movies')
#     language = models.CharField(max_length=20)
#     cast = models.CharField(max_length=100)
#     movie_trailer = models.FileField(upload_to='movies')
#     views_count = models.IntegerField(default=0)
#     year_of_production = models.DateField()
#     created = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.title


class Profile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user = models.CharField(max_length=100, blank=True)
	bio = models.TextField(default="no bio....", max_length=1000)
	email = models.EmailField(max_length=200, blank=True)
	image = models.ImageField(default='avatar.png', upload_to='img/')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	# def get_friends(self):
	# 	return self.friends.all()

	# def get_friends_no(self):
	# 	return self.friends.all().count()

	# def get_posts_no(self):
	# 	return self.posts.all().count()

	# def get_all_authors_posts(self):
	# 	return self.posts.all()	

	# def get_likes_given_no(self):
	# 	liked = self.likes_set.all()
	# 	total_liked = 0
	# 	for item in liked:
	# 		if item.value =='Like':
	# 			total_liked += 1
	# 		return total_liked

	# def get_likes_given_no(self):
	# 	likes = self.likes_set.all()
	# 	total_liked = 0
	# 	for item in likes:
	# 		if item.value=='Like':
	# 			total_liked += 1
	# 		return total_liked	
	
	# def get_likes_received_no(self):
	# 	posts = self.posts.all()
	# 	total_liked = 0
	# 	for item in posts:
	# 		total_liked += item.liked.all().count()
	# 	return total_liked					
			

	# def __str__(self):
		# return f"{self.user.username}--{self.created.strftime('%d-%m-%Y')}"

	# def save(self, *args, **kwargs):
	# 	ex = False
	# 	if self.first_name and self.last_name:
	# 		to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
	# 		ex = Profile.objects.filter(slug=to_slug).exists()
	# 		while ex:
	# 			to_slug = slugify(to_slug + " " + str(get_random_code()))
	# 			ex = Profile.objects.filter(slug=to_slug).exists()
	# 	else:
	# 		to_slug = str(self.user)
	# 	self.slug = to_slug
	# 	super().save(*args, **kwargs)	

