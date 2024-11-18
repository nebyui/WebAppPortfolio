# views.py

from django.shortcuts import render, HttpResponse
from .models import Image
from .models import Program

# Views act like the specific web page
# Handles rendering HTML pages and requesting data from the database

def home(request): # Defines Home view, returns home page
    return render(request, "home.html")

def art_gallery(request): # Defines art gallery view, returns art gallery page
    images = Image.objects.all() # Retrieves all the items in Image database
    return render(request, "art_gallery.html", {"Images": images}) # Retrieves the corresponding HTML page and image objects

def programming_projects(request): # Same thing but for the programs
    programs = Program.objects.all() 
    return render(request, "programming_projects.html", {"Programs": programs})
