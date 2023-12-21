from django.test import TestCase
from django.contrib.auth.models import User
from topics.models import *


# Create your tests here.


class RoutingTest(TestCase):
    urls = {
        'top': '/',
        'post': '/civicSeek_app/post/',
        'postcomment-1': '/civicSeek_app/postcomment/1/',
        'postdone': '/civicSeek_app/postdone/',
        'ranking': '/civicSeek_app/ranking/',
        'showpost-1': '/civicSeek_app/showpost/1/',
        'toolbar': '/civicSeek_app/toolbar/',

        # 'afterlogin'と'beforelogin'は'top'ビュー関数を作成し'/'に変更した

        # create_account_done
        'signup_success': '/accounts/signup_success/',
        # create_an_account
        'signup': '/accounts/signup/',
        # profileを表示する
        'profile': '/accounts/profile/',
        # edit_profile
        'edit_profile': '/accounts/edit_profile/',
        # login
        'login': '/accounts/login/',
    }

    def setUp(self):
        # ユーザーを作成
        self.user = User.objects.create_user(
            username='testuser',
            email='test_test@test.com',
            password='testpassword',
            date_joined='2020-01-01 00:00:00',
        )

    def test_should_return_200_when_access_to_top(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['top'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_post(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['post'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_postcomment(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['postcomment-1'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_postdone(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['postdone'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_ranking(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['ranking'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_showpost(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        # response = self.client.get(self.urls['showpost-1'])
        response = self.client.get('/civicSeek_app/showpost/1/')
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_toolbar(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['toolbar'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_signup_success(self):
        # self.client.login(username='testuser', password='testpassword',email='test_test@test.com')
        response = self.client.get(self.urls['signup_success'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_signup(self):
        # self.client.login(username='testuser', password='testpassword',email='test_test@test.com')
        response = self.client.get(self.urls['signup'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_profile(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['profile'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_edit_profile(self):
        self.client.login(username='testuser',
                          password='testpassword', email='test_test@test.com')
        response = self.client.get(self.urls['edit_profile'])
        self.assertEqual(response.status_code, 200)

    def test_should_return_200_when_access_to_login(self):
        # self.client.login(username='testuser', password='testpassword',email='test_test@test.com')
        response = self.client.get(self.urls['login'])
        self.assertEqual(response.status_code, 200)
