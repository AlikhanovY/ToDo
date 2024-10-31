from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm, UserRegistrationForm, UserLoginForm
from .models import Item
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def profile_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        print("post")
        if form.is_valid():
            print("valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authentication = authenticate(request, username=username, password=password)

            if authentication is not None:
                login(request, authentication)
                print("logged in")
                return redirect('profile')

    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def list_items(request):
    user = request.user
    items = Item.objects.filter(author=user.profile)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = user.profile
            item.save()
            items = Item.objects.filter(author=user.profile)
            return render(request, 'items.html', {'items': items, 'form': ItemForm()})

    form = ItemForm()
    return render(request, 'items.html', {"items": items, 'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
