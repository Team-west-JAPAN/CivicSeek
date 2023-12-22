from django.urls import path, reverse_lazy
from .views import SignupView
from django.contrib.auth.views import *
from accounts.views import *

app_name = "accounts"

signup_view = SignupView.as_view(template_name='accounts/signup.html')
login_view = CustomLoginView.as_view()
logout_view = LogoutView.as_view(
    template_name='accounts/logout.html', redirect_field_name='top')
password_change_view = PasswordChangeView.as_view(
    template_name='accounts/password_change.html',
    success_url=reverse_lazy('accounts:password_change_done'))
password_change_done_view = PasswordChangeDoneView.as_view(
    template_name='accounts/password_change_done.html')
password_reset_view = PasswordResetView.as_view(
    template_name='accounts/password_reset.html')
password_reset_done_view = PasswordResetDoneView.as_view(
    template_name='accounts/password_reset_done.html')
password_reset_confirm_view = PasswordResetConfirmView.as_view(
    template_name='accounts/password_reset_confirm.html')
password_reset_complete_view = PasswordResetCompleteView.as_view(
    template_name='accounts/password_reset_complete.html')

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password_change/', password_change_view, name='password_change'),
    path('password_change/done/', password_change_done_view,
         name='password_change_done'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('password_reset/done/', password_reset_done_view,
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view,
         name='password_reset_confirm'),
    path('reset/done/', password_reset_complete_view,
         name='password_reset_complete'),
    path('signup_success/', signup_success, name='signup_success'),
    path('signup/', signup_view, name='signup'),

    path('profile/', profile_view, name='profile_view'),
    path('edit_profile/', edit_profile_view, name='edit_profile_view')
]
