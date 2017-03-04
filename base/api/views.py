# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shortener.models import Shortener
from rest_framework import viewsets
from .serializers import ShortenerListSerializers


class ShortenerListViewset(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerListSerializers
