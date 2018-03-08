from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by('date');  ### sort articles by date//// send articles to the template so we can output data through template
    return render(request, 'articles/article_list.html', { 'articles': articles }) ### the data we want to send to template, key name can be changed.
