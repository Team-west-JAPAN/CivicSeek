"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from civicSeek_app.views import top

urlpatterns = [
    path('', top, name='top'),
    path('admin/', admin.site.urls),
    path('topics/', include('topics.urls')),
    path('general/', include('general.urls')),
    path('accounts/', include('accounts.urls')),
    path('ranking/', include('ranking.urls')),
    # path('testapp/', include('testapp.urls')),


    # これはフロントと合わせるためのラッパーコード
    path('civicSeek_app/', include('civicSeek_app.urls')),
]
