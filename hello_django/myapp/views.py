from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from myapp.forms import MyForm

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World!')

def homepage(request):
    return HttpResponse('Welcome to Ayiv Kab Django')

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style='color:#F4CE14;'>Welcome to Ayiv Django</h1>"""
    return HttpResponse(text)

def form_view(request):
    form =MyForm()
    context = {"form": form}
    return render(request, "home.html", context)

    