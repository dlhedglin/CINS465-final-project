from django import forms
from .models import static_image, Picture, Mails
from custom_user.models import MyUser

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = static_image
        fields = ['img'] 
    def save(self, request):
        image_instace = static_image()
        image_instace.img = self.cleaned_data['img']
        image_instace.artist = request.user
        image_instace.save()
        return image_instace

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Mails
        fields = ['artist','email','name','content','document'] 
    content = forms.CharField( widget=forms.Textarea(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'id': "clientemail"}))
    name = forms.CharField( widget=forms.TextInput(attrs={'class': "form-control"}))

class changeProfilePictureForm(forms.Form):
    picture = forms.ImageField()