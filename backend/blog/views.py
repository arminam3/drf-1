from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Article

class ArticleListView(generic.ListView):
    template_name = 'blog/article_list'
    context_object_name = 'articles'

    def get_queryset(self):
        articles = Article.objects.filter(status=True)
        return articles

class ArticleDetail(generic.DetailView):
    def get_object(self):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs['pk'])
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'