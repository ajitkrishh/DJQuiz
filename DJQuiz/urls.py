
from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path("" , include("Quiz.urls")),
    path('admin/', admin.site.urls),
    path("account/" , include('myauth.urls')),


    
]
