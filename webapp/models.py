# models.py

from django.db import models
    
# Creates SQLite Databases


class Image(models.Model): # Creates art image database, each item has a title and image file
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="art_images/", blank=True) # Where added images are uploaded to in server files
    
class Program(models.Model): # Creates database for programming projects
    title = models.CharField(max_length=200)
    demoLink = models.URLField(max_length=1000, blank=True) # Link to YouTube video demonstration
    demoLink2 = models.URLField(max_length=1000, blank=True)
    gitLink = models.URLField(max_length=1000, blank=True) # Link to GitHub project repository
