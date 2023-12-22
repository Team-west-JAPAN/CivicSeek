from django.shortcuts import render
from general.views import *
from ranking.views import *
from topics.views import *
from topics.models import *
from civicSeek_app.models import *


# Create your views here.
# このビューの目標 : 今まで作ってきたバックエンドのラッパーコードを作成し、構造を簡潔にする。

def top(request):
    '''
    トップ画面をレンダリングする関数だから
    今後はtop.htmlを新たに作って、それをレンダリングする
    top.htmlに移植完了
    '''
    # 一応これで動かす
    # topics = get_object_or_404(Topic) # 存在するすべての投稿された課題
    topics = Topic.objects.all()  # 存在するすべての投稿された課題
    context = {
        'topics': topics,
    }

    return render(request, 'html/top.html', context=context)


@login_required
def post(request):
    '''
    投稿画面をレンダリングする関数だから
    # ラッパー先改変完了
    # ラッパーの実装は完了
    '''
    # tepmalteの場所を定義
    template_name = 'html/post.html'
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

        # 成功時はpostdoneへリダイレクト
        return redirect('postdone')

    # POST等が場合は以下を実行して、template_nameをレンダリング
    return render(request, template_name, context={"username": user.username})

@login_required
def postcomment(request, topic_id: int):
    '''
    コメント画面を投稿する関数だから
    topicsアプリのcreate_commentをラッパー
    # ラッパー先改変完了
    '''
    '''
    投稿表示画面(コメント投稿)
    '''
    template_name = 'html/postcomment.html'
    topic = get_object_or_404(Topic, pk=topic_id)
    # comments = Comment.objects.filter(commented_to=topic)
    comments = get_object_or_404(Comment).filter(commented_to=topic)

    user = request.user  # ログインしているユーザーのオブジェクト

    if request.method == "POST":
        '''コメントが投稿されたら
        '''

        # コメントの格納
        comment_instance = Comment.objects.create(
            comment=request.POST.get('comment'),
            created_by=user,
            commented_to=topic)

        # DBに保存
        comment_instance.save()

        # 自分自身にリダイレクトして画面リロード
        return redirect(reverse('postcomment', args=[topic_id]))

    return render(request, template_name, context={'topic': topic, 'comments': comments, 'username': user.username})


def postdone(request):
    '''
    投稿完了画面をレンダリングする関数だから
    topicsアプリのcomplete_create_topicをラッパー
    # ラッパー先改変完了
    '''
    '''
    投稿完了画面
    '''
    # return complete_create_topic(request)
    template_name = 'html/postdone.html'
    return render(request, template_name)


def ranking(request):
    '''
    ランキング画面をレンダリングする関数だから
    rankingアプリのrankingをラッパー
    # ラッパー先改変完了
    '''
    return show_ranking(request)


def showpost(request, topic_id: int):
    '''
    投稿表示画面をレンダリングする関数だから
    topicsアプリのdetail_topicをラッパー
    # ラッパー先改変完了
    # この関数自体を改変完了
    投稿表示画面
    '''
    template_name = 'html/showpost.html'
    # topic = Topic.objects.get(pk=topic_id)
    topic = get_object_or_404(Topic, pk=topic_id)

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
            return redirect(reverse(TOP_PAGE_NAME))  # トップ画面にリダイレクト

    return render(request, template_name, context={'topic': topic})


@login_required
def profile(request):
    '''
    この関数は作ってなかったな
    '''
    user = request.user
    context = {
        'username': user.username,
        'date_joined': user.date_joined,
        'email': user.email,
    }

    return render(request, 'html/profile.html', context=context)


def faq_view(request):
    '''
    よくある質問のリンク先
    '''
    faqs = Faq.objects.all()

    return render(request, 'html/faq.html', context={'faqs': faqs})
