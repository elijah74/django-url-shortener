# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .baseconv import Base62


@python_2_unicode_compatible
class Shortener(models.Model):
    """
    shortener 관련 테이블
    """
    INACTIVE, ACTIVE = (0, 1)
    STATUS_CHOICES = (
        (INACTIVE, _('inactive')),
        (ACTIVE, _('active')),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    link_url = models.URLField(max_length=255, blank=False, null=False)
    status = models.SmallIntegerField(_('status'), choices=STATUS_CHOICES,
                                      default=ACTIVE)

    class Meta:
        verbose_name = _('shortener')
        verbose_name_plural = _('shorteners')

    def __str__(self):
        return "{}".format(self.link_url)

    def short_url(self):
        return "{}/{}".format(settings.SHORTENER_DOMAIN, Base62.encode(self.pk))
