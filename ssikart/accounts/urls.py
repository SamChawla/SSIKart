from django.urls import path

from accounts.views import (activate, dashboard, forgot_password, login,
                            logout, register, reset_password,
                            resetpassword_validate)

urlpatterns = [
    path("register/", register, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("dashboard/", dashboard, name="dashboard"),
    # Forget Password Urls
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/", reset_password, name="reset_password"),
    path(
        "resetpassword_validate/<uidb64>/<token>/",
        resetpassword_validate,
        name="resetpassword_validate",
    ),
]
