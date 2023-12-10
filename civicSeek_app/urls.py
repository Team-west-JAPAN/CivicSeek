from django.urls import path
from civicSeek_app.views import *

urlpatterns = [
    path('post/', post, name='post'),
    path('postcomment/<int:topic_id>/', postcomment, name='postcomment'),
    path('postdone/', postdone, name='postdone'),
    path('ranking/', ranking, name='ranking'),
    path('showpost/<int:topic_id>/', showpost, name='showpost'),
    path('toolbar/', toolbar, name='toolbar'),
]

