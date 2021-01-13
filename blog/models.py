# from __future__ import unicode_literals
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save#, request_finished
from django.dispatch import receiver

from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import now
# from .forms import *
import uuid
from .utils import random_string_generator, unique_slug_generator
from django.db.models import Q
from simple_history.models import HistoricalRecords

class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(title_icontains=query) | Q(content_icontains=query) | Q(author_icontains=query))
            qs = qs.filter(or_lookup.distinct())
        return qs


class PostManager(models.Manager):
     def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(blank=True, default='Guest', max_length=75)
    # image = models.ImageField(default='avatar.png', upload_to='images/')
    slug = models.SlugField(blank=True, null=True, unique=True)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    history = HistoricalRecords() 

    class Meta:
        ordering = ["-timeStamp", "-sno"]

    def save_without_historical_record(self, *args, **kwargs):
        self.skip_history_when_saving = True
        try:
            ret = self.save(*args, **kwargs)
        finally:
            del self.skip_history_when_saving
        return ret    

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


    def get_all_authors_posts(self):
      return self.posts.all() 


        
    # def save(self, *args, **kwargs):
    #     if not self.slug :
    #         self.slug = slugify(self.title or self.sno )
    #     super(Post , self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)#, self.sno)
    #     super(Post, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title + ', by: ' + self.author


    def create_slug(instance, new_slug=None):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug
        qs = Post.objects.filter(slug=slug).order_by("-sno")
        exists = qs.exists()
        if exists:
            new_slug = "%s-%s" %(slug, qs.first().sno)
            return create_slug(instance, new_slug=new_slug)
        return slug

    # objects = PostManager()

@receiver(pre_save, sender=Post)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = Post)



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    class Meta:
        ordering = ["-timestamp"]

    

    def __str__(self):
        return self.comment[0:13] + "..." + "by " + self.user.username



# class AddToDatabase(models.Model):
#     user_input = models.CharField(max_length=50, unique=True)
#     random_url = models.UUIDField(default=uuid.uuid4)