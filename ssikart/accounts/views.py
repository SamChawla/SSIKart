from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from accounts.models import Account


# Create your views here.
def register(request):
    form = RegistrationForm()
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = email.split("@")[0]

            user = Account.objects.create_user(first_name, last_name, username, email, password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful !')
            return redirect('registration')
            form = RegistrationForm()

    context_data = {
        "form": form
    }
    return render(request, 'accounts/register.html', context_data)


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')