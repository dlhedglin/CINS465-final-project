from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Picture, static_image, Mails
from custom_user.admin import UserCreationForm
from custom_user.models import MyUser
from .forms import UploadFileForm, ImageForm, ContactForm, changeProfilePictureForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.conf import settings
from . import scrape
from mysite.settings import BASE_DIR, MEDIA_URL

def index(request):
    artists = MyUser.objects.all()
    data = {
        'artists': artists,
    }
    return render(request, 'home.html', context=data)

def chat(request):
    return render(request, 'myapp/chat.html')

def room(request, room_name):
    return render(request, 'myapp/rooms.html', {
        'room_name': room_name
    })

def aftercare(request):
    return render(request, 'aftercare.html')

def destiny(request):
    return render(request, 'destiny.html')

def contact(request, userId = ''):    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print("yes valid")
            post = form.save(commit=False)
            post.save()
            contact_name = request.POST.get('name','')
            contact_email = request.POST.get('email', '')
            contact_artist = request.POST.get('artist','')            
            form_content = request.POST.get('content', '')
            document = request.FILES.get('document')
            artist = MyUser.objects.all()
            
            for obj in artist:               
                if str(obj.pk) == contact_artist:
                    artist_email = obj.email
            
            template = get_template('contact_template.txt')
            context = {
                'contact_artist': contact_artist,
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            email_from = settings.EMAIL_HOST_USER
            email = EmailMessage("Consolation Appointment",
                    content,
                    email_from,
                    [artist_email])
            if document:
                tempdoc = Mails.objects.all()
                print(BASE_DIR + MEDIA_URL)
                document = tempdoc[0].document
                email.attach_file(BASE_DIR + MEDIA_URL + str(document))
            email.send()
            Mails.objects.all().delete()
            
                       
        return redirect('/')
    else:
        if userId != '':
            artist = MyUser.objects.filter(id=userId)
            if len(artist) != 0:
                artist = artist[0]
                form = ContactForm(initial={'artist': artist})
            else:
                form = ContactForm
        else:
            form = ContactForm
        return render(request, 'contactus.html',{
            'form':form,
    })    
    
def artistpage(request, user_id):
    artistObject = MyUser.objects.filter(id=user_id)[0]
    static_images = static_image.objects.filter(artist=artistObject)
    # insta_images = Picture.objects.filter(artist=artistObject)
    if(artistObject.instagram_name):
        insta_images = scrape.get_shared_data(artistObject.instagram_name)
        insta_images = scrape.extractLinks(insta_images)
    else:
        insta_images = []
    form = ImageForm
    profileForm = changeProfilePictureForm
    data = {
        'artist': artistObject,
        'form': form,
        'profile_form': profileForm,
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

def changeProfilePicture(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = changeProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['picture'])
            user = MyUser.objects.get(pk=request.user.id)
            user.profile_picture = form.cleaned_data['picture']
            user.save()
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