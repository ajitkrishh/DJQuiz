from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib import messages
from myauth.forms import CustomUserRegistration

# Create your views here.


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
