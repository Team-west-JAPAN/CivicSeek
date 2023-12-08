from django.shortcuts import render, get_object_or_404, redirect
from topics.models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.html import escape
from django.http import HttpResponse
from topics.models import Topic
from topics.models import Topic, Comment, Tag
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from accounts.forms import ProfileEdit, SignUpForm, CustomLoginForm


# Create your views here.


def signup_success(request):
    # 会員登録成功画面
    '''アカウント
    '''
    template_name = 'accounts/signup_success.html'
    return render(request, template_name)


class CustomLoginView(LoginView):
    app_name = "accounts"
    authentication_form = CustomLoginForm
    form_class = CustomLoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "ログインに成功しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ログインに失敗しました")
        return super().form_invalid(form)


class SignupView(CreateView):
    app_name = "accounts"
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, "ユーザー登録しました。")
        self.object = user
        # return HttpResponseRedirect(self.get_success_url())
        return render(request=self.request, template_name='accounts/signup_success.html')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "ユーザー登録に失敗しました。")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定するためのget_success_urlメソッドをオーバーライドします。
    def get_success_url(self):
        # ログアウト後にリダイレクトしたいURLを指定します。
        return reverse_lazy('home')  # このURLをカスタマイズしてください


def profile_view(request):
    '''profileの表示をする
    '''
    if request.method == "POST":
        '''何かのボタンが押されたら
        '''
        if "edit_profile" in request.POST:
            '''編集ボタンが押されたら
            '''
            return redirect('accounts:edit_profile_view')

    return render(request, 'accounts/profile.html', {'user': request.user})


def edit_profile_view(request):
    '''profileの編集ページ
    '''
    if request.method == 'POST':
        '''何らかのボタンが押されたら
        '''
        if "save_profile" in request.POST:
            pass
            form = ProfileEdit(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile_view')  # プロフィールページにリダイレクト
        else:
            form = ProfileEdit(instance=request.user)  # ここは要検討
    else:
        form = ProfileEdit(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})


# Create your views here.


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


# Create your views here.


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
UserModel = get_user_model()


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
