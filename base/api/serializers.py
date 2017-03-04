# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from shortener.models import Shortener


class ShortenerListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shortener
        fields = ('short_url', 'link_url', 'status')
