from django.shortcuts import render, redirect
from topics.models import * 
from django.http import HttpResponse
from django.utils.html import escape
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from config.settings import TOP_PAGE_NAME

# Create your views here.
UserModel = get_user_model()


def detail_topic(request, topic_id):
    '''
    投稿表示画面
    '''
    template_name = 'html/showpost.html'
    topic = Topic.objects.get(pk=topic_id)

    if request.method == "POST":
        if "button_like" in request.POST:
            '''いいねが押された時
            '''
            topic.like_count += 1 # とりあえず+1にしてる
            topic.save()
        elif "button_comment" in request.POST:
            '''コメントが押された時
            '''
            return redirect(reverse('create_comment',args=[topic_id]))
        elif "button_delete_comment" in request.POST:
            '''削除ボタンが押された時
            '''
            topic.delete()
            return redirect(reverse(TOP_PAGE_NAME)) # トップ画面にリダイレクト

    return render(request, template_name, context={'topic': topic})

@login_required
def create_comment(request, topic_id):
    '''
    投稿表示画面(コメント投稿)
    '''
    template_name = 'html/postcomment.html'
    topic = Topic.objects.get(pk=topic_id)
    comments = Comment.objects.filter(commented_to=topic)
    user = request.user # ログインしているユーザーのオブジェクト

    if request.method == "POST":
        '''コメントが投稿されたら
        '''

        # コメントの格納
        comment_instance = Comment.objects.create(
            comment = request.POST.get('comment'),
            created_by = user,
            commented_to = topic)

        # DBに保存
        comment_instance.save()

        # 自分自身にリダイレクトして画面リロード
        return redirect(reverse('postcomment',args=[topic_id]))


    return render(request, template_name,context={'topic':topic,'comments':comments,'username':user.username})

@login_required
def create_topic(request):
    '''
    投稿画面
    '''
    # tepmalteの場所を定義
    template_name = 'html/post.html'
    user = request.user # ログインしているユーザーのユーザー名

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
        return redirect('postdone')

    # POST等が場合は以下を実行して、template_nameをレンダリング
    return render(request, template_name,context={"username":user.username})

@login_required
def complete_create_topic(request):
    '''
    投稿完了画面
    '''
    template_name = 'html/postdone.html'
    return render(request, template_name)
