from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Article


#def index(request):
#    articles = Article.objects.all()
#    return render(request, 'blogapp/index.html',{'articles':articles})
class IndexList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blogapp/index.html'

# def article_page(request, article_id):
#     article = Article.objects.get(pk=article_id)
#     return render(request,"blogapp/article_page.html",{'article':article})
class PageView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blogapp/article_page.html'

# def edit_page(request,article_id):
#     if str(article_id) == '0':
#         return render(request,'blogapp/edit_page.html')
#     article = Article.objects.get(pk=article_id)
#     return render(request,'blogapp/edit_page.html',{'article':article})

# def edit_action(request):
#     title = request.POST.get('title','TITLE')
#     content = request.POST.get('content','CONTENT')
#     article_id = request.POST.get('article_id','0')
#     if article_id == '0':
#         Article.objects.create(title=title,content=content)
#         articles = Article.objects.all()
#         return render(request, 'blogapp/index.html',{'articles':articles})
#     article = Article.objects.get(pk=article_id)
#     article.title = title
#     article.content = content
#     article.save()
#     return render(request,"blogapp/article_page.html",{'article':article})