from django.db import models

# Create your models here.


class Faq(models.Model):
    """
    FAQのモデル -> これは管理者が作成する
    """
    question = models.CharField(max_length=200)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
