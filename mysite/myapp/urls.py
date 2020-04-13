from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('artists/<int:user_id>', views.artistpage, name='artistpage'),
    path('upload_image/', views.upload_image),
    path('login/', auth_views.LoginView.as_view(), {'next_page': '/'}),
    path('logout/', views.logout_user),
<<<<<<< HEAD
=======
    path('Contact/', views.contact, name='contact'),
    path('remove_image/<int:image_id>', views.remove_image)
>>>>>>> 476641ef60f799367ebc2d1c3dab680eeba9e7b9
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)