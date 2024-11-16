# urls.py

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="Home"),
    path ("art_gallery/", views.art_gallery, name="Art Gallery"),
    path("programming_projects/", views.programming_projects, name="Programming Projects")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)