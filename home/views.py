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

from .models import Profile
from .forms import ProfileModelForm
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.views import View
from django.urls import reverse
from .utils import token_generator
from django.utils import translation
from django.utils.translation import gettext as _
from django.conf import settings
from django.db.models import Q

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.contrib.sites.shortcuts import get_current_site
import threading
from pytube import YouTube
from pytube import Playlist
import os
import geopy
from geopy.geocoders import Nominatim

import requests
# import netifaces as nif
import re, uuid
from getmac import get_mac_address as gma
import argparse
from django.db.models import Count
import speedtest
# import requests 
import pandas as pd 
from bs4 import BeautifulSoup
from ipaddress import ip_address 
import socket    
import re
import struct
import textwrap
from datetime import datetime, timedelta

from plyer import notification


######### nltk Tutorial ############ 
import nltk
import nltk.corpus
from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
fdist = FreqDist()
from nltk.tokenize import blankline_tokenize
from nltk.util import *
from nltk.stem import PorterStemmer
pst = PorterStemmer()
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
from nltk.stem import SnowballStemmer
sbst = SnowballStemmer('english')
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()
from nltk.corpus import stopwords
import re
punctuation = re.compile(r'[-.?!,:;()|0-9]')
from nltk import ne_chunk

# allPosts = Post
# Create your views here.

class EmailThread(threading.Thread):

	def __init__(self, email):
		self.email=email
		threading.Thread.__init__(self)

	def run(self):
		self.email.send()	

def home(request):
	user_language = {}
	translation.activate(user_language)
	request.session[translation.LANGUAGE_SESSION_KEY] = user_language

	# if translation.LANGUAGE_SESSION_KEY in request.session:
	# 	del request.session[translation.LANGUAGE_SESSION_KEY]

	title = _('Homepage')

	allPosts = Post.objects.order_by('-views', '-timeStamp')[:3]
	context = {'allPosts': allPosts, 'title': title}
	return render(request, 'home/index.html', context)


def about(request):
	return render(request, 'home/about.html')


def contact(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['name']
			email = request.POST['email']
			phone = request.POST['phone']
			content = request.POST['content']

			if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
				messages.error(request, "Please fill the form correctly")
				notification.notify(
					title='Please fill form correctly',
					message='Fill the all requirements correctly before submit the form.',
					app_icon='C:\\Users\\Rohit\\Desktop\\iCoder-Upgrade\\static\\img\\error.ico',
					timeout=5
				)
			else:
				contact = Contact(name=name, email=email, phone=phone, content=content)
				contact.save()
				messages.success(request, "Your message has been successfully sent")
				notification.notify(
					title='Your message has been successfully sent',
					message='You entered Messages are sent successfully',
					app_icon='C:\\Users\\Rohit\\Desktop\\iCoder-Upgrade\\static\\img\\success.ico',
					timeout=5
				)
		return render(request, 'home/contact.html')		
	else:
		messages.error(request, 'Your are not Logged In! Please login to Contact Me')
		return render(request, 'home/contact.html')




def search(request, *args, **kwargs):
	query = request.GET['query']
	tokenize = word_tokenize(query)
	# print(tokenize)

	############# Not Working in the website ############ 
	# for word in tokenize:
	#  	fdist[word.lower()]+=1
	# print(fdist)
	# print(fdist(query))

	########### END / #########################

	Query_blank = blankline_tokenize(query)
	# print(len(Query_blank))
	quotes_tokens = nltk.word_tokenize(query)
	# print(quotes_tokens)
	quotes_bigrams = list(nltk.bigrams(quotes_tokens))
	# print(quotes_bigrams)
	# print(pst.stem(query))
	# print(stopwords.words('english'))
	# print(len(stopwords.words('english')))
	post_punctuation = []
	for words in tokenize:
	    word = punctuation.sub("",words)
	    if len(word)>0:
	        post_punctuation.append(word)

	# print(post_punctuation)

	NE_token = word_tokenize(query)
	NE_tags = nltk.pos_tag(NE_token)
	NE_NER = ne_chunk(NE_tags)
	# print(NE_NER)

	new_tokens = nltk.pos_tag(word_tokenize(query))
	# print(new_tokens)

	token = tokenize, Query_blank
	# print(token)
	# allPosts = Post.token.filter(title=query)

	result = {}




	# allPosts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(author__icontains=query))
	
	# params = {'allPosts': allPosts, 'query': query}
	return render(request, 'home/search.html')
	# return HttpResponse("Searching..")

def handleSignup(request):
	if request.method == 'POST':
		username = request.POST['username']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		if len(username) > 10:
			messages.error(request, "Username must be under 10 characters.")
			return redirect('home')

		if not username.isalnum():
			messages.error(request, "Username should only contain letter and numbers.")
			return redirect('home')	

		if pass1 != pass2:
			messages.error(request, "Passwords do not match.")
			return redirect('home')
	    
	    # if not User.objects.filter(username=username).exists():
	    # 	messages.error(request, 'Your Username is Already Taken')

	    # if not User.objects.filter(email=email).exists():
	    # 	messages.error(request, 'Your email is Taken by other')


		myuser = User.objects.create_user(username, email, pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		# myuser.is_active = False
		myuser.save()

		# uidb64 = urlsafe_base64_encode(force_bytes(myuser.pk))

		# domain = get_current_site(request).domain

		# link=reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(myuser)})

		# email_subject = 'Activate your Account'

		# activate_url = 'http://'+domain+link
		# email_body = 'Hi ' +myuser.username + ' Please use the link to verify your account\n ' + activate_url
		# email = EmailMessage(
		#     email_subject,
		#     email_body,
		#     'noreplay@store.com',
		#     [email],
		# )

		# email.send(fail_silently=False)

		EmailThread(email).start()
		# messages.success(request, "Your iCoder account has been created Successfully created")
		messages.success(request, "Your account was successfully created at iCoder")
		return redirect('/')
	else:
		return HttpResponse('404 Page Not Found')	


class VerificationView(View):
	def get(self, request, uidb64, token):
		try:
			id = force_text(urlsafe_base64_decode(uidb64))
			myuser = User.objects.get(pk=id)

			if not token_generator.check_token(myuser, token):
				messages.error(request, 'Account already activated. Go to login')
				return redirect('/')

			if myuser.is_active:
				return redirect('/')
			myuser.is_active = True
			myuser.save()

			messages.success(request, 'Account activated Successfully '+myuser.username+' go forward to iCoder')
			return redirect('/')

		except expression as identifier:
			pass	
		return HttpResponse("activation page")



def LoginView(request, *args, **kwargs):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']

		user = authenticate(email=email, password=password) 
		if user:
			if user.is_active:
				login(request, user)
				messages.success(request, 'Successfully Logged in as '+user.username)
				return redirect('/')
			else:
				messages.error(request, "Account not activate.Please check your email.")
				return redirect('/')
	return render(request, 'home/login_user.html')	


# @staff_member_required
def handleLogin(request, *args):
	if request.method == 'POST':
		loginusername = request.POST['loginusername']
		loginpass = request.POST['loginpass']

		user = authenticate(username=loginusername, password=loginpass) 

		# if user is not None:
		# 	login(request, user)
		# 	messages.success(request, "Successfully Logged In as "+user.username)
		# 	return redirect("home")
		# else:
		# 	messages.error(request, "invalid credentials. Please try again")
		# 	return redirect('home')	
		if user:
			if user.is_active:
				login(request, user)
				messages.success(request, 'Successfully Logged in as '+user.username)
				return redirect('/')
			else:
				messages.error(request, "Account not activate.Please check your email.")
				return redirect('/')

	return HttpResponse("404 Page Not Found")	


def handleLogout(request):
	logout(request)
	messages.success(request, "Successfully Logged Out.")
	return redirect('home')	


# def login(request, *args, **kwargs):
# 	return HttpResponse('Login page')



def my_profile_view(request, *args, **kwargs):
	profile = Profile.objects.get()
	# pro = Profile.objects.get(user=request.user)
	form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
	confirm = False

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			confirm = True

	context = {
		'profile': profile,
		'form': form,
		'confirm': confirm,
	}
	return render(request, 'home/profile.html', context)
	# return HttpResponse('Thhis is Profile page')






url = ''

def DownYtd_Video(request):
	
	print('url :', url)
	
		
	# print('resolution: ',resolutions)	
	return render(request, 'home/Down_YTD.html')


def Download_Video(request):
	global url
	url = request.GET.get('url')
	if request.user.is_authenticated:
		try:
			obj = YouTube(url)
			resolutions = []
			strm_all = obj.streams.filter(progressive=True, file_extension='mp4')
			for i in strm_all:
				resolutions.append(i.resolution)
			resolutions = list(dict.fromkeys(resolutions))
			embed_url = url.replace("watch?v=", "embed/")
			path = 'C:\\Users\\Rohit\\Downloads'
			return render(request, 'home/download.html', {'rsl': resolutions, 'embed': embed_url, 'url': url})
		except:
			return HttpResponse("<h3>Sorry Invalid Format or Invalid Url ?</h3>")
	else:
		return redirect('home')		


def download_complete(request, res):
	global url
	if request.user.is_authenticated:
		homedir = os.path.expanduser("~")
		dirs = homedir + '\\Downloads'
		print(f'DIRECT: ', f"{dirs}")
		if request.method == "POST":
			YouTube(url).streams.get_by_resolution(res).download(dirs)
			messages.success(request, "Download complete!. Please check out video")
			# messages.error(request, "Invalid Things.Please try again?.")
			return redirect('/')
		else:
			messages.error(request, "Invalid Things.Please try again?.")
			return HttpResponse("<h3>Download Not Complete. Please try Again!.</h3>")
	else:
		return redirect('home')			



def geolocator(request, *args, **kwargs):
	if request.user.is_authenticated:
		return render(request, 'home/geo.html')
	else:
		# return render(request, 'home/index.html')
		messages.error(request, "Your are not Logged In!. That's You are not avail the geo location")
		return redirect('home')
			

def geo_loc(request, *args, **kwargs):

	text = request.GET['zipCode']

	geolocator = Nominatim(user_agent="geoapiExercises")
	location = geolocator.geocode(text)
	context = {
			'location': location,
			'text': text,
			'gma': gma
		}

	return render(request, 'home/geo_loc.html', context)

	


def stringError(request, slug):
	# return redirect('home')
	return render(request, 'home/error.html')


def speedTest(request, *args, **kwargs):
	st = speedtest.Speedtest()
	# option = int(request.GET.get('option'))
	# print(type(option))

	# if option == 1:
		# print(type(option))
		# print(st.download())

	return render(request, 'home/speed.html')



def getdata(url):
    	r = requests.get(url)
    	return r.text	


def get_fuel_rate(request, *args, **kwargs):
	htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
	soup = BeautifulSoup(htmldata, 'html.parser')

	mydatastr = ''
	result = []

	# searching all tr in the html data 
	# storing as a string 
	for table in soup.find_all('tr'): 
	    mydatastr += table.get_text() 
  
	# set accourding to your required 
	mydatastr = mydatastr[1:] 
	itemlist = mydatastr.split("\n\n")
  
	for item in itemlist[:-5]: 
	    result.append(item.split("\n")) 
  
	# Calling DataFrame constructor on list 
	df = pd.DataFrame(result[:-8])

	context = {
		'df': df
	}

	return render(request, 'home/fuel.html', context)



def setcookie(request):
	response = render(request, 'home/setcookie.html')
	response.set_signed_cookie('name', 'rahul', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
	return response


def getcookie(request, *args, **kwargs):
	name = request.get_signed_cookie('name', salt='nm')
	context = {
		'nm': name,
	}
	return render(request, 'home/getcookie.html', context)


def delcookie(request):
	response = render(request, 'home/delcookie.html')
	response.delete_cookie('name')
	return response



