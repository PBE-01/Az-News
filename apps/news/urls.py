from django.urls import path
from apps.news.views import HomeView, DetailNewsView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name ='home'),
    path('details/<int:news_id>', DetailNewsView.as_view(), name ='detail'),
]