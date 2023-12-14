from django.shortcuts import render, get_object_or_404
from topics.models import Topic

# Create your views here.


def show_ranking(request):
    topics = Topic.objects.all().order_by('-like_count')[:3]
    return render(request, 'html/ranking.html', context={'topics': topics})
