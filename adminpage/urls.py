# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from .views import *


__author__ = "Epsirom"


urlpatterns = [
    url(r'^login$', Login.as_view()),
    url(r'^logout$', Logout.as_view()),
    url(r'^activity/list$', ActivityList.as_view()),
    url(r'^activity/delete$', ActivityDelete.as_view()),
    url(r'^activity/create$', ActivityCreate.as_view()),
    url(r'^activity/detail$', ActivityDetails.as_view()),
    url(r'^image/upload$',UploadImg.as_view()),
    url(r'^activity/menu$',ActivityMenu.as_view()),
    url(r'^activity/checkin$',CheckIn.as_view()),
]
