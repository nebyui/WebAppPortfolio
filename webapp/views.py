# views.py

from django.shortcuts import render, HttpResponse
from .models import Image
from .models import Program

def home(request):
    return render(request, "home.html")

def art_gallery(request):
    images = Image.objects.all()
    return render(request, "art_gallery.html", {"Images": images})

def programming_projects(request):
    programs = Program.objects.all()
    return render(request, "programming_projects.html", {"Programs": programs})
