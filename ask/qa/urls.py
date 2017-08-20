from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.mainpage, name="home"),
	url(r"^login/", views.test, name="login"),
	url(r"^signup/", views.test, name="signup"),
	url(r"^question/(?P<id>\d+)/", views.questions, name="question"),
	url(r"^ask/", views.test, name="ask"),
	url(r"^popular/", views.populars, name="popular"),
	url(r"^new/", views.test, name="new"),
	url(r"^create/", views.create, name="create")
]
