from django.urls import path

from accounts.views import activate, login, logout, register

urlpatterns = [
    path("register/", register, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
]
