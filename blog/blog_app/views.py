from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# # Create your views here.
# def index(request):
#    return render(request, 'blog_app/index.html')

from django.views import generic
from .models import Post # Postモデルをimport

class IndexView(generic.TemplateView):
    template_name = 'blog_app/index.html'

class PostListView(generic.ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し