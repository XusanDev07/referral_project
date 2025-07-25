from django.urls import path
from .views import SendCodeView, VerifyCodeView, ProfileView, UseInviteCodeView

urlpatterns = [
    path('send-code/', SendCodeView.as_view()),
    path('verify-code/', VerifyCodeView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('use-invite/', UseInviteCodeView.as_view()),
]
