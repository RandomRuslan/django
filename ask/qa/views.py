# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from qa.models import Question, Answer
from django.contrib.auth.models import User
import random

def test(request, *args, **kwargs):
    return HttpResponse('RuslanCHIK')

@require_GET
def mainpage(request):
    post = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 10)
    page = paginator.page(page)
    paginator.baseurl = "/?page="
    return render(request, 'templates/list_of_questions.html', {
        'post' : page.object_list,
        'paginator' : paginator,
        'page' : page,
    })

@require_GET
def populars(request):
    post = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 10)
    page = paginator.page(page)
    paginator.baseurl = "/popular/?page="
    return render(request, 'templates/list_of_questions.html', {
        'post' : page.object_list,
        'paginator' : paginator,
        'page' : page,
    })

def questions(request, id):
    try:
        post = Question.objects.get(id=int(id))
    except:
        raise Http404
    return render(request, 'templates/question.html', {
        'post' : post,
    })

def create(request):
    for i in range(48):
        q = Question.objects.create(
            title = "Title "+str(i),
            text =  "Some text " + str(random.randint(i*10,(i+1)*10)),
            rating = random.randint(1,100),
            author = User.objects.create_user('userjohn'+str(i), 'lennon'+str(i)+'@thebeatles.com', 'john'+str(i)+'password')
        )
    return "<html><body>200 OK :)</body></html>"
