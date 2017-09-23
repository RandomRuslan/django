# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    def save(self):
        return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
    def save(self):
        #params = dict(self.cleaned_data)
        params = {"text" : self.cleaned_data["text"], "author" : self.cleaned_data["author"]}
        params["question_id"] = self.cleaned_data["question"]
        return Answer.objects.create(**params)

class UserForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    def save(self):
        return User.objects.create_user(**self.cleaned_data)
