# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM Question ORDER BY added_at DESC")
		return cursor.fetchall()
	def popular(self):
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM Question ORDER BY rating DESC")
		return cursor.fetchall()

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
	
