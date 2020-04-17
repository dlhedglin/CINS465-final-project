from django import forms
from .models import *
from . import models
from custom_user import models

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

class ContactForm(forms.Form):

    contact_artist = forms.ModelChoiceField(queryset = MyUser.objects.all(),required=True)
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required = True)
    content = forms.CharField(
        required = True,
        widget = forms.Textarea
    )