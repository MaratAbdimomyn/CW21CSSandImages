from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OneView.as_view(), name='home'),
    path('about/<int:pk>/', AboutView.as_view(), name='about'),
    path('create_image', add_image, name='create_image'),
    path('search', search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)