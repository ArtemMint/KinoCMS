from django.urls import path
from register.views.user import login_page, UserRegisterView, userUpdateView
from register.views.password import PasswordChangeView, PasswordSuccessView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('register/', UserRegisterView.as_view(), name='register'),
                  path('login/', login_page, name='login'),
                  path('profile/edit', userUpdateView, name='edit_profile'),
                  path('password/', PasswordChangeView.as_view()),
                  path('password/success', PasswordSuccessView.as_view(), name='password_success'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
