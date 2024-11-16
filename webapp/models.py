# models.py

from django.db import models
    
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="art_images/", blank=True)
    
class Program(models.Model):
    title = models.CharField(max_length=200)
    program = models.FileField(upload_to="programming_projects/", blank=True)
