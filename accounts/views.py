from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    error = None
    username_value = ""
    if request.method == "POST":
        username_value = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username_value, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get("next") or "home"
            return redirect(next_url)
        error = "Credenziali non valide. Verifica username e password."

    form = AuthenticationForm(request=request)
    return render(
        request,
        "accounts/login.html",
        {"form": form, "error": error, "username_value": username_value},
    )


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")
