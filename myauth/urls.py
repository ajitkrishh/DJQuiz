from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomTokenObtainPairView, My_LoginView,registration,Registerview
# rest
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login',My_LoginView.as_view() , name = 'login'),
    path('register', registration,name = "register"),
    path('logout', LogoutView.as_view(),name = "logout"),

    # rest urls
    path('api/register', Registerview.as_view(),name = "aregister"),
    path('api/login', CustomTokenObtainPairView.as_view(), name='alogin'),
    path('api/token-refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
