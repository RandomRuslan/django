# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django import forms
from qa.models import Question, Answer

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

