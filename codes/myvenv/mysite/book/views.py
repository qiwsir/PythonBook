from django.shortcuts import render
from .models import Articles

def book_title(request):  
    posts = Articles.objects.all()  
    return render(request, "book/titles.html", {"posts":posts})  

def book_article(request, article_id):
    article = Articles.objects.get(id=article_id)
    return render(request, 'book/content.html', {"article": article})