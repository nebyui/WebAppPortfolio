# admin.py

from django.contrib import admin
from .models import Image
from .models import Program

# Adds models / databases to the admin page, where the admin can add each item

admin.site.register(Image)
admin.site.register(Program) 