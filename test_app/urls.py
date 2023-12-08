from django.urls import path
from test_app.views import *

urlpatterns = [
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
