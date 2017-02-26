# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import UrlRedirect


urlpatterns = [
    url(r'^(?P<key>\w+)/$', UrlRedirect.as_view(), name='urlredirect'),
]
