from django.test import TestCase
from civicSeek_app.models import *

# Create your tests here.
UserModel = get_user_model()

class SignUpTest(TestCase):
    def test_do_contain_specified_text(self):
        """'/accounts/signup/'のレスポンスに'会員登録'という文字列が入っているかテスト,andそのレスポンスのステータスコードが200であるかテスト
        """
        response = self.client.get('/accounts/signup/')
        self.assertContains(response,"会員登録",status_code=200)

    def test_is_use_template(self):
        """テンプレートとして'accounts/signup.html'を使用しているかテスト
        """
        response = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(response,'accounts/signup.html')



class HomeTest(TestCase):
    def test_should_return_200_statuscode(self):
        '''
        home page test
        '''
        response = self.client.get('/general/home/')
        self.assertEqual(response.status_code,200)


class Complete_create_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        '''
        complete create topic status code test
        '''
        response = self.client.get('/topics/complete_create_topic/')
        self.assertEqual(response.status_code, 200)


class Create_comment_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        '''
        create comment status code test
        '''
        response = self.client.get(f'/topics/1/create_comment/')
        self.assertEqual(response.status_code, 200)


class Create_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        '''
        create topic status code test
        '''
        response = self.client.get('/topics/create_topic/')
        self.assertEqual(response.status_code, 200)


class Detail_topic_test(TestCase):
    def test_should_return_200_httpstatus_code(self):
        '''
        detail topic status code test
        '''
        response = self.client.get('/topics/detail_topic/1/')
        self.assertEqual(response.status_code, 200)
