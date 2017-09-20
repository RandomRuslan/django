from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r"^$", views.show_mainpage, name="home"),
	url(r"^login/", views.login_user, name="login"),
	url(r"^signup/", views.signup, name="signup"),
	url(r"^question/(?P<id>\d+)/", views.show_question, name="question"),
	url(r"^ask/", views.ask, name="ask"),
	url(r"^popular/", views.show_populars, name="popular"),
	url(r"^new/", views.show_mainpage, name="new"),
	url(r"^create/", views.create, name="create"),
	url(r"^logout/", views.logout_user, name="logout")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
