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
        self.cleaned_data["question_id"] = self.cleaned_data["question"]
        return Answer.objects.create(**self.cleaned_data)

class UserForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    def save(self):
        return User.objects.create(**self.cleaned_data)
