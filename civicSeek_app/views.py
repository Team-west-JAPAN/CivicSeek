from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.html import escape
from django.http import HttpResponse
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.shortcuts import render, redirect
from django.views import View
from civicSeek_app.models import *


# Create your views here.
UserModel = get_user_model()


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


# Create your views here.


def show_ranking(request):
    topics = Topic.objects.all().order_by('-like_count')[:3]
    return render(request, 'ranking/show_ranking.html', context={'topics': topics})


# Create your views here.


def detail_topic(request, topic_id):
    '''
    投稿表示画面
    '''
    template_name = 'topics/detail_topic.html'
    topic = Topic.objects.get(pk=topic_id)

    if request.method == "POST":
        if "button_like" in request.POST:
            '''いいねが押された時
            '''
            topic.like_count += 1  # とりあえず+1にしてる
            topic.save()
        elif "button_comment" in request.POST:
            '''コメントが押された時
            '''
            return redirect(reverse('create_comment', args=[topic_id]))
        elif "button_delete_comment" in request.POST:
            '''削除ボタンが押された時
            '''
            topic.delete()
            return redirect(reverse('home'))

    return render(request, template_name, context={'topic': topic})


@login_required
def create_comment(request, topic_id):
    '''
    投稿表示画面(コメント投稿)
    '''
    template_name = 'topics/create_comment.html'
    topic = Topic.objects.get(pk=topic_id)
    comments = Comment.objects.filter(commented_to=topic)
    user = request.user  # ログインしているユーザーのオブジェクト

    if request.method == "POST":
        '''コメントが投稿されたら
        '''

        # コメントの格納
        comment_instance = Comment.objects.create(
            comment=request.POST.get('comment'),
            created_by=user,  # change to `created_by = request.user`
            commented_to=topic)

        # DBに保存
        comment_instance.save()

        # 自分自身にリダイレクトして画面リロード
        return redirect(reverse('create_comment', args=[topic_id]))

    return render(request, template_name, context={'topic': topic, 'comments': comments, 'username': user.username})


@login_required
def create_topic(request):
    '''
    投稿画面
    '''
    # tepmalteの場所を定義
    template_name = 'topics/create_topic.html'
    user = request.user  # ログインしているユーザーのユーザー名

    if request.method == "POST":  # 押されたボタンに関わらずPOSTされた時に実行
        '''
        ここはバリデーションやサニタイズが必要
        '''
        # リクエストから入力データを取得
        title = request.POST.get('title')
        description = request.POST.get('description')

        # バリデーション : タイトルと説明が空でないことを確認
        if not title or not description:
            return HttpResponse("タイトルと説明は必須です.")

        # サニタイズ
        title = escape(title)
        description = escape(description)

        # モデルインスタンスの生成
        topic = Topic.objects.create(
            title=title,
            description=description,
            created_by=user  # ここは変更しないといけない
        )

        # データベースに保存
        topic.save()

        # 成功時はcomplate_create_topicへリダイレクト
        return redirect('complate_create_topic')

    # POST等が場合は以下を実行して、template_nameをレンダリング
    return render(request, template_name, context={"username": user.username})


@login_required
def complete_create_topic(request):
    '''
    投稿完了画面
    '''
    template_name = 'topics/complete_create_topic.html'
    return render(request, template_name)

# Create your views here.
# これはテスト用にレンダリングを行うコード
######################################## START ########################################


def afterlogin(request):
    return render(request, 'html/afterlogin.html')


def beforelogin(request):
    return render(request, 'html/beforelogin.html')


def create_account_done(request):
    return render(request, 'html/create_account_done.html')


def create_an_account(request):
    return render(request, 'html/create_an_acccount.html')


def edit_profile(request):
    return render(request, 'html/edit_profile.html')


def login(request):
    return render(request, 'html/login.html')


def postcomment(request):
    return render(request, 'html/postcomment.html')


def postdone(request):
    return render(request, 'html/postdone.html')


def post(request):
    return render(request, 'html/post.html')


def ranking(request):
    return render(request, 'html/ranking.html')


def showpost(request):
    return render(request, 'html/showpost.html')


def toolbar(request):
    return render(request, 'html/toolbar.html')


######################################## END ########################################
