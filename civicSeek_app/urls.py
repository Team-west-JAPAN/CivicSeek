from django.urls import path
from civicSeek_app.views import *

urlpatterns = [
    path('post/', post, name='post'),
    path('postcomment/<int:topic_id>/', postcomment, name='postcomment'),
    path('postdone/', postdone, name='postdone'),
    path('ranking/', ranking, name='ranking'),
    path('showpost/<int:topic_id>/', showpost, name='showpost'),
    path('profile/', profile, name='profile'),
    path('faq/', faq_view, name='faq'),
    path('liked_count/', liked_topics, name='liked_topics'),
]
