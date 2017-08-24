# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import *
from django.contrib.auth.models import User
import random

def test(request, *args, **kwargs):
    return HttpResponse('RuslanCHIK')

@require_GET
def show_mainpage(request):
    question = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 10)
    page = paginator.page(page)
    paginator.baseurl = "/?page="
    return render(request, 'templates/list_of_questions.html', {
        'question' : page.object_list,
        'paginator' : paginator,
        'page' : page,
    })

@require_GET
def show_populars(request):
    question = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(question, 10)
    page = paginator.page(page)
    paginator.baseurl = "/popular/?page="
    return render(request, 'templates/list_of_questions.html', {
        'question' : page.object_list,
        'paginator' : paginator,
        'page' : page,
    })

def show_question(request, id):
    try:
        id = int(id)
        question = Question.objects.get(id=id)
    except:
        raise Http404
    if request.method == "POST":
        form = AnswerForm({"text" : request.POST["text"], "question" : id})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/question/%d/" % id)
    else:
        form = AnswerForm()
    return render(request, "templates/question.html", {'question' : question, 'form' : form})

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect("/question/%d" % question.id)
    else:
        form = AskForm()
    return render(request, "templates/ask.html", {'form' : form})

def create(request):
    try:
        user = User.objects.create(username="Ruslan", password="password")
    except:
        user = User.objects.get(username="Ruslan")
    for i in range(21):
        q = Question.objects.create(
            title = "Title "+str(i),
            text =  "Some text " + str(random.randint(i*10,(i+1)*10)),
            rating = random.randint(1,100),
            author = user
        )
    return HttpResponse('Question was added')
