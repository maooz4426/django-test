# from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'blog_app/index.html')