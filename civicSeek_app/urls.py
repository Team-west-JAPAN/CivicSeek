# coding:utf-8
from django.urls import path
from django.contrib.auth.views import *
from civicSeek_app.views import *


urlpatterns = [
    # ホーム
    path('home/', home, name='home'),

    # ユーザprofile
    path('profile/', profile_view, name='profile_view'),
    path('edit_profile/', edit_profile_view, name='edit_profile_view'),

    path('show_ranking/', show_ranking, name='show_ranking'),

    # 課題を投稿する機能
    path('complete_create_topic/', complete_create_topic,
         name='complate_create_topic'),
    path('<int:topic_id>/create_comment/',
         create_comment, name='create_comment'),
    path('create_topic/', create_topic, name='create_topic'),
    path('detail_topic/<int:topic_id>/', detail_topic, name='detail_topic'),
]
