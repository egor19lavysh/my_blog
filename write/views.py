from django.shortcuts import render
from .forms import ArticleForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():

            article = form.save(commit=False)
            article.author = request.user
            article.save()

            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = ArticleForm()
    
    return render(request, "write/writing.html", {"form" : form})
