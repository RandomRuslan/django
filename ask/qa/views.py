# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from qa.models import Answer, Question
from qa.forms import AnswerForm, AskForm, UserForm
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
    return render(request, 'list_of_questions.html', {
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
    return render(request, 'list_of_questions.html', {
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
    error = ''
    if request.method == "POST":
        form = AnswerForm({"text" : request.POST["text"], "question" : id})
        if form.is_valid():
            if request.user.is_authenticated():
                form.cleaned_data["author"] = request.user
                form.save()
                return HttpResponseRedirect("/question/%d/" % id)
            else:
                error = "You must be authenticated"
                return render(request, "login.html", {'error' : error})
    form = AnswerForm()
    return render(request, "question.html", {'question' : question, 'form' : form})

def ask(request):
    error = ''
    if request.method == "POST":    
        form = AskForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                form.cleaned_data["author"] = request.user
                question = form.save()
                return HttpResponseRedirect("/question/%d" % question.id)
            else:
                error = "You must be authenticated"
                return render(request, "login.html", {'error' : error})
    form = AskForm()
    return render(request, "ask.html", {'form' : form})

def signup(request):
    error = ''
    if request.method == "POST":                
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(username=request.POST.get("username"))
            except User.DoesNotExist:
                user = form.save()
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = "This name is reserved"
    form = UserForm()
    return render(request, "signup.html", {'form' : form, 'error' : error})

def login_user(request):
    error = ''
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            error = "Incorrect username/password"

    return render(
request, "login.html", {'error' : error})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
    
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
    return HttpResponse('Questions was added')
