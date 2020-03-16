from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<int:user_id>', views.artistpage, name='artistpage'),
    path('upload_image/', views.upload_image),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)