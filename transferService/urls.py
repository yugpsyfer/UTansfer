from django.urls import path

from . import views
from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    # path('upload/', views.upload, name='upload'),
    path('upload_file/', views.upload_file, name='upload_file')

] #+ static(settings.STORAGE_URL, document_root = settings.STORAGE_ROOT)