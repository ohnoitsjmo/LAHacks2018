from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$',                    views.login,   name='login'),
    url(r'^get_idioms/$',      views.get_idioms,      name='get_idioms'),
    ]
