from django.shortcuts import render
from .forms import UserRegisterForm
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:

        register_form = UserRegisterForm()
    return render(request, "users/register.html", {'register_form': register_form})


def profile(request):
    return render(request, 'users/profile.html')
