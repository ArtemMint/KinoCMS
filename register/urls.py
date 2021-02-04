from django.urls import path
from register.views.user import login_page, UserRegisterView, UserEditView
from register.views.password import PasswordChangeView, PasswordSuccessView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', login_page, name='login'),
    path('profile/edit', UserEditView.as_view(), name='edit_profile'),
    path('password/change', PasswordChangeView.as_view()),
    path('password/success', PasswordSuccessView.as_view(), name='password_success'),
]