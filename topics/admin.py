from django.contrib import admin
from topics.models import Topic,Comment

# Register your models here.

admin.site.register([Topic,Comment])