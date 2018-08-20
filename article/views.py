from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.
'''
def article_detail(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
        context={}
        context['article_ojb']=article
        #return render(request,"article_detail.html",context)
        return render_to_response("article_detail.html",context)
    except Article.DoesNotExist:
        raise Http404("不存在")
    #return HttpResponse("<h2>文章标题：%s</h2><h3>文章内容：%s</h3>" % (article.title,article.content))
'''
def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    context={}
    context['article_ojb']=article
    return render_to_response("article_detail.html",context)

def article_list(request):
    articles=Article.objects.filter(is_deleted=False)
    context={}
    context['articles']=articles
    return render_to_response("article_list.html",context)