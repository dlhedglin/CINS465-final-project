from django import forms
from .models import *
from . import models

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = static_image 
        fields = ['img'] 
    def save(self, request):
        image_instace = models.static_image()
        image_instace.img = self.cleaned_data['img']
        image_instace.artist = request.user
        image_instace.save()
        return image_instace