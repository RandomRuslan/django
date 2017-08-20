# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
    return HttpResponse('RuslanCHIK')

@require_GET
def mainpage(request):
    post = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    paginator.baseurl = "/?page="
    return render(request, 'qa/list_of_questions.html', {
        'post' : post,
        'paginator' : paginator,
        'page' : page,
    })

@require_GET
def populars(request):
    post = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    page = paginator.page(page)
    paginator.baseurl = "/popular/?page="
    return render(request, 'qa/list_of_questions.html', {
        'post' : post,
        'paginator' : paginator,
        'page' : page,
    })

def questions(request, id):
    try:
        post = Question.objects.get(id=int(id))
    except:
        raise Http404
    return render(request, 'qa/question.html', {
        'post' : post,
    })

