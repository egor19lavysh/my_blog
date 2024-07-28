from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect

class ArticlesList(ListView):
    paginate_by = 5
    ordering=['-publishing_date']
    template_name = "main/index.html"
    model = models.Article

    
    
class ArticleDetail(DetailView):
    template_name = "main/detail.html"
    model = models.Article
