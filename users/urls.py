from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Login API
    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),

    # Refresh token API
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]