from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Artist, Picture

def index(request):
    artists = Artist.objects.all()
    data = {
        'artists': artists
    }
    return render(request, 'home.html', context=data)
    
def artistpage(request, first_name, last_name):
    artistObject = Artist.objects.filter(first_name=first_name, last_name=last_name)
    print(artistObject.values())
    return HttpResponse(artistObject) 

# Create your views here.
