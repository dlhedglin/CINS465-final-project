from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Picture, static_image
from custom_user.admin import UserCreationForm
from custom_user.models import MyUser
from .forms import UploadFileForm, ImageForm

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm
    else:
        form = ImageForm
    artists = MyUser.objects.all()

    data = {
        'artists': artists,
        'form': form,
    }
    return render(request, 'home.html', context=data)
    
def artistpage(request, user_id):
    artistObject = MyUser.objects.filter(id=user_id)
    static_images = static_image.objects.filter(artist=artistObject[0])
    insta_images = Picture.objects.filter(artist=artistObject[0])
    form = ImageForm
    data = {
        'users': artistObject,
        'form': form,
        'static_images': static_images,
        'insta_images': insta_images,
        'user_id': user_id
    }
    return render(request, 'artistpage.html', context=data)

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
    return redirect('/artists/' + str(request.user.id))

# Create your views here.
