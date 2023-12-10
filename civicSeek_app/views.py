from django.shortcuts import render
from general.views import *
from ranking.views import *
from topics.views import *
from topics.models import *


# Create your views here.


def top(request):
    '''
    トップ画面をレンダリングする関数だから
    とりあえず、html/beforelogin.htmlをレンダリングする
    今後はtop.htmlを新たに作って、それをレンダリングする
    '''
    topics = Topic.objects.all()  # 存在するすべての投稿された課題
    context = {
        'topics': topics,
    }

    return render(request, 'html/beforelogin.html', context=context)


def post(request):
    '''
    投稿画面をレンダリングする関数だから
    topicsアプリのcreate_topicsをラッパー
    '''
    return create_topic(request)


def postcomment(request, topic_id: int):
    '''
    コメント画面を投稿する関数だから
    topicsアプリのcreate_commentをラッパー
    '''
    return create_comment(request, topic_id)


def postdone(request):
    '''
    投稿完了画面をレンダリングする関数だから
    topicsアプリのcomplete_create_topicをラッパー
    '''
    return complete_create_topic(request)


def ranking(request):
    '''
    ランキング画面をレンダリングする関数だから
    rankingアプリのrankingをラッパー
    '''
    return ranking(request)


def showpost(request, topic_id: int):
    '''
    投稿表示画面をレンダリングする関数だから
    topicsアプリのdetail_topicをラッパー
    '''
    return detail_topic(request, topic_id)


def toolbar(request):
    '''
    この関数は作ってなかったな
    '''
    return render(request, 'html/toolbar.html')


# アカウント関連の話はaccountsに一任ってことで

# def afterlogin(request):
#     return render(request, 'afterlogin.html')
#
#
# def beforelogin(request):
#     return render(request, 'beforelogin.html')
#
#
# def create_account_done(request):
#     return render(request, 'create_account_done.html')
#
#
# def create_an_account(request):
#     return render(request, 'create_an_account.html')
#
#
# def edit_profile(request):
#     return render(request, 'edit_profile.html')
#
#
# def login(request):
#     return render(request, 'login.html')
