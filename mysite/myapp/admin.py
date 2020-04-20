from django.contrib import admin
from .models import Picture, static_image, Mails
# Register your models here.

admin.site.register(Picture)
admin.site.register(static_image)
admin.site.register(Mails)