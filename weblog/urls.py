#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from weblog.views import PostList

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
]
