from django.shortcuts import render
from django.views.generic import TemplateView
from apps.news.models import News, NewsCategory

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        categories = NewsCategory.objects.filter(is_active=True)
        most_news = News.objects.filter(is_active=True).order_by('-created_at')[0]
        news1 = News.objects.filter(is_active=True).order_by('-created_at')[1:4]
        news2 = News.objects.filter(is_active=True).order_by('-created_at')[4:9]
        context.update({
            'user' : user,
            'categories' : categories,
            'most_news' : most_news,
            'news1' : news1,
            'news2' : news2
        })
        return context

class DetailNewsView(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news_id = self.kwargs.get('news_id')
        news = News.objects.filter(id=news_id, is_active=True).first()

        context['news'] = news

        return context