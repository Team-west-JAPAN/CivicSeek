from django.shortcuts import render
from topics.models import Topic, Comment, Tag

# Create your views here.


def top(request):
    '''
    テスト用のトップページ
    '''
    template_name = 'general/top.html'
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }
    return render(request, template_name, context)


def home(request):
    '''ログイン前・後HOME
    '''
    template_name = 'general/home.html'
    topics = Topic.objects.all()
    context = {
        'topics': topics
    }

    return render(request, template_name, context)
