from telnetlib import LOGOUT
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'hello.html', {'name': 'salwa'})

