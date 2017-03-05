# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer
from shortener.models import Shortener


class ShortenerSerializers(ModelSerializer):

    class Meta:
        model = Shortener
        fields = ('short_url', 'link_url', 'status')
