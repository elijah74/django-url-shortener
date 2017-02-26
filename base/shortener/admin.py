# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shortener


@admin.register(Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'link_url', 'status', 'created')
    fields = ('short_url', 'link_url', 'status', 'created', 'modified')
    readonly_fields = ('short_url', 'created', 'modified')

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        instances.link_url = instances.link_url.rstrip()
        formset.save_m2m()
