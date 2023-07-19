from typing import Any, Dict
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib import messages
from myauth.forms import CustomUserRegistration
from .models import User

# rest_framework
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer, UserRegistrationSerializer



class My_LoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse("topiclist")
   

def registration(req):
    if req.method == "POST":
        form = CustomUserRegistration(req.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            for field_errors in form.errors.values():
                for error in field_errors:
                    messages.error(req, error)
            return render(req, "registration/signup.html", {"form": form})

    elif req.method == "GET":
        form = CustomUserRegistration()
        return render(
            req,
            "registration/signup.html",
        )

# for rest register
class Registerview(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = request.data
        refresh = RefreshToken.for_user(user)

        response_data = {
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
        return Response(response_data)

# views.py

from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


