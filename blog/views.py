from django.shortcuts import render, get_object_or_404
from .models import BlogArticles
# Create your views here.


def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'titles.html', {'blogs':blogs})
# render用于页面渲染


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "content.html", {"article": article, "publish": pub})
# 处理因为ID不存在引起的报错