# https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError
from myapp.models import Artist, Picture
import requests
import json

BASE_URL = 'https://www.instagram.com/'

# modified from https://github.com/rarcega/instagram-scraper/
def get_shared_data(username=''):
        """Fetches the user's metadata."""
        resp = requests.get(BASE_URL + username).text
        if resp is not None and '_sharedData' in resp:
            try:
                shared_data = resp.split("window._sharedData = ")[1].split(";</script>")[0]
                return json.loads(shared_data)
            except (TypeError, KeyError, IndexError):
                pass
def getUserId(username):
    return get_shared_data(username)['entry_data']['ProfilePage'][0]['graphql']['user']['id']

def extractLinks(shared_data):
    links = []
    for edge in shared_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']:
        link = edge['node']['display_url']
        links.append(link)
    return links

class Command(BaseCommand):
    help = 'Collects pictures from artists instagram accounts'
    def handle(self, *args, **options):
        artists = Artist.objects.all()
        if(len(artists) == 0):
            return
        for i in artists:
            instagram_name = i.insta_name
            if(instagram_name != ''):
                tempArtist = i
                shared_data = get_shared_data(instagram_name)
                image_links = extractLinks(shared_data)
                for i in image_links:
                    print(len(i))
                    p = Picture(picture_url=i, artist=tempArtist)
                    p.save()
                self.stdout.write(self.style.SUCCESS('Successfully collected images for "%s"' % instagram_name))