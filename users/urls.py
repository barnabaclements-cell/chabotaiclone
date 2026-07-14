from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import DebugUserView



urlpatterns = [

    path(
        "login/",
        TokenObtainPairView.as_view(),
        name="login"
    ),


    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),


    # TEMPORARY DEBUG
    path(
        "debug-user/",
        DebugUserView.as_view()
    ),

]