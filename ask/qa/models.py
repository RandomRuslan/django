# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, connection
from django.contrib.auth.models import User
from django import forms
import random

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-id")
	def popular(self):
		return self.order_by("-rating")

class Question(models.Model):
	title = models.CharField(max_length=255)
	text =  models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name="question_likes_user")
	objects = QuestionManager()
	def __unicode__(self):
		return self.title
	class Meta:
		db_table = "Question"
	

class Answer(models.Model):
	text =  models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	def __unicode__(self):
		return self.text
	class Meta:
		db_table = "Answer"

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    def save(self):
        try:
            user = User.objects.create(username="Ruslan", password="password")
        except:
            user = User.objects.get(username="Ruslan")
        params = dict(self.cleaned_data)
        params["author"] = user
        question = Question.objects.create(**params)
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
    def save(self):
        try:
            user = User.objects.create(username="Ruslan", password="password")
        except:
            user = User.objects.get(username="Ruslan")
        params = {"text" : self.cleaned_data["text"]}
        params["author"] = user
        params["question_id"] = self.cleaned_data["question"]
        answer = Answer.objects.create(**params)
        return answer
