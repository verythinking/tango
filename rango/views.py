# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context_dict = {
        'boldmessage': 'I am bold font from the context'
    }
    return render(request, 'rango/index.html', context_dict)
