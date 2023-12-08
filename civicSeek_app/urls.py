# coding:utf-8
from django.urls import path
from django.contrib.auth.views import *
from civicSeek_app.views import *


urlpatterns = [
    # ホーム
    path('home/', home, name='home'),

    path('show_ranking/', show_ranking, name='show_ranking'),

    # 課題を投稿する機能
    path('complete_create_topic/', complete_create_topic,
         name='complate_create_topic'),
    path('<int:topic_id>/create_comment/',
         create_comment, name='create_comment'),
    path('create_topic/', create_topic, name='create_topic'),
    path('detail_topic/<int:topic_id>/', detail_topic, name='detail_topic'),


    # テスト用のレンダリングルーティング
    path('afterlogin/', afterlogin, name='afterlogin'),
    path('beforelogin/', beforelogin, name='beforelogin'),
    path('create_account_done/', create_account_done, name='create_account_done'),
    path('create_an_account/', create_an_account, name='create_an_account'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('login/', login, name='login'),
    path('postcomment/', postcomment, name='postcomment'),
    path('postdone/', postdone, name='postdone'),
    path('post/', post, name='post'),
    path('ranking/', ranking, name='ranking'),
    path('showpost/<int:topic_id>', showpost, name='showpost'),
    path('toolbar/', toolbar, name='toolbar'),
]
