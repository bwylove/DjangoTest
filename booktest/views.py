# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.

def index(request):
    temp=loader.get_template('booktest/index.html')
    return HttpResponse(temp.render())