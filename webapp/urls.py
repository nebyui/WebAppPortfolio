# urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Defines rouding and URL paths to the views
# Adding these paths to end of URL takes client to the corresponding view (aka web page)


urlpatterns = [
    path("", views.home, name="Home"),
    path ("art_gallery/", views.art_gallery, name="Art Gallery"), # (URL path, view, name of URL to be referenced in templates)
    path("programming_projects/", views.programming_projects, name="Programming Projects")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Contains path information to the images, which is a "static" element