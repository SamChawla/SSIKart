from django.urls import path
from accounts.views import register, login, logout


urlpatterns = [
    path('register/', register, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]

