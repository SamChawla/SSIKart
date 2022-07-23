from django.urls import path

from accounts.views import (activate, change_password, dashboard, edit_profile,
                            forgot_password, login, logout, my_orders, order_detail,
                            register, reset_password, resetpassword_validate)

urlpatterns = [
    path("register/", register, name="registration"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
    path("dashboard/", dashboard, name="dashboard"),
    
    path('my_orders/', my_orders, name='my_orders'),
    path('edit_profile/', edit_profile, name='edit_profile'), 
    path('change_password/', change_password, name='change_password'),

    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),

    # Forget Password Urls
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/", reset_password, name="reset_password"),
    path(
        "resetpassword_validate/<uidb64>/<token>/",
        resetpassword_validate,
        name="resetpassword_validate",
    ),
]
