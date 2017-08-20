# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-added_at")
	def popular(self):
		return self.order_by("-rating")

class Question(models.Model):
	title = models.CharField(max_length=255)
	text =  models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User, related_name="question_likes_user")
	objects = QuestionManager()
	def __unicode__(self):
		return self.title
    class Meta:
		db_table = "Question"
	
class Answer(models.Model):
	text =  models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.OneToOneField(Question)
	author = models.OneToOneField(User)
	def __unicode__(self):
		return self.title
	class Meta:
        db_table = "Answer"
	
