# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from shortener.models import Shortener
from rest_framework import viewsets
from .serializers import ShortenerSerializers


class ShortenerViewset(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializers
