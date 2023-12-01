from django.shortcuts import render, redirect

# Create your views here.


def afterlogin(request):
    return render(request, 'html/afterlogin.html')


def beforelogin(request):
    return render(request, 'html/beforelogin.html')


def create_account_done(request):
    return render(request, 'html/create_account_done.html')


def create_an_account(request):
    return render(request, 'html/create_an_account.html')


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
