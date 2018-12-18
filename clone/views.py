from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import redirect
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    return render(request, "home.html",)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user)

    return render(request, "profile.html", {"images":images})