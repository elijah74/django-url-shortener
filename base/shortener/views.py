# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.views import generic

from .baseconv import Base62
from .models import Shortener


class UrlRedirect(generic.RedirectView):

    model = Shortener

    def get_redirect_url(self, *args, **kwargs):
        key = kwargs.get('key', None)
        if key is None:
            raise Http404
        try:
            pk = Base62.decode(key)
        except:
            raise Http404

        object = self.get_object(pk)
        return object.link_url

    def get_object(self, pk):
        try:
            object = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
        if object.status == object.INACTIVE:
            raise Http404
        return object
