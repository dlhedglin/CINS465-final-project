from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Picture, static_image
from custom_user.admin import UserCreationForm
from custom_user.models import MyUser
from .forms import UploadFileForm, ImageForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.conf import settings

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

def contact(request):
    form_class = ContactForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',
                ''
            )
            contact_email = request.POST.get(
                'contact_email',
                ''
            )
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            email_from = settings.EMAIL_HOST_USER

            send_mail(
                "Consolation Appointment",
                content,
                email_from,
                ['tattootestemail@gmail.com'],
                # headers = {'Reply-To': contact_email},
            )            

            return redirect('contact')

    return render(request, 'contactus.html',{
        'form':form_class,
    })    
    
def artistpage(request, user_id):
    artistObject = MyUser.objects.filter(id=user_id)[0]
    static_images = static_image.objects.filter(artist=artistObject)
    insta_images = Picture.objects.filter(artist=artistObject)
    form = ImageForm
    data = {
        'artist': artistObject,
        'form': form,
        'static_images': static_images,
        'insta_images': insta_images,
        'user_id': user_id
    }
    return render(request, 'artistpage.html', context=data)

def upload_image(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request)
    else:
        return redirect('/login')
    return redirect('/artists/' + str(request.user.id))

def remove_image(request, image_id):
    if request.user.is_authenticated:
        foundImage = static_image.objects.filter(id=image_id)
        if foundImage:
            if foundImage.values()[0]['artist_id'] == request.user.id:
                foundImage.delete()
                return redirect('/artists/' + str(request.user.id))
            else:
                return HttpResponse('You cannot remove another users image')
    else:
        return redirect('/')



def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
    return