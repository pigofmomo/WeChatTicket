# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from .views import *


__author__ = "Epsirom"


urlpatterns = [
    url(r'^login$', Login.as_view()),
    url(r'^logout$', Logout.as_view()),
    url(r'^activity/list$', ActivityList.as_view()),

]
