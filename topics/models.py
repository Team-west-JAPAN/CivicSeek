# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


UserModel = get_user_model()


class Topic(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=100)
    description = models.TextField(verbose_name="概要")
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    # models.PROTECTをしていすると投稿者が消えてもトピックを消さないようにできる.
    # ここではmodels.CASCADEを指定し、投稿者のアカウントが消えると投稿も消えるようにする
    created_by = models.ForeignKey(UserModel,
                                   related_name='topics_account',
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE,
                                   default=None,
                                   null=True,
                                   blank=True)
    tags = TaggableManager(blank=True)
    like_count = models.IntegerField(default=0)

    class Meta:
        db_table = "topics"

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    # 下のcreated_atはauto_now_add=Trueにしてしまうと,編集された時も更新されるため、変数名的に適切ではない.から消した
    # 今回は編集をしないためauto_now_add=Trueを指定
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(UserModel,
                                   related_name='comments_account',
                                   verbose_name="投稿者",
                                   on_delete=models.CASCADE)
    commented_to = models.ForeignKey(Topic,
                                     related_name='topics',
                                     verbose_name="トピック",
                                     on_delete=models.CASCADE)

    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comment
