from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from django.urls import path

from .views import RegistrationAPIView, UserModelViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token_refresh/', TokenRefreshView.as_view()),
    path('users/', UserModelViewSet, name='all_users'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
]
