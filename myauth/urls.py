from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import My_LoginView,registration
urlpatterns = [
    path('login',My_LoginView.as_view() , name = 'login'),
    path('register', registration,name = "register"),
    path('logout', LogoutView.as_view(),name = "logout"),
]
