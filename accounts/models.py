from django.db import models
# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from topics.models import Topic
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_student = models.BooleanField(default=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    liked_topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class Notification(models.Model):
#     '''ユーザーアカウントにone2oneで紐づいた通知を格納する
#     '''
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     notification = models.TextField(max_length=500, blank=True)

class Notification(models.Model):
    '''ユーザーアカウントに紐づいた通知を格納する
    '''
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
