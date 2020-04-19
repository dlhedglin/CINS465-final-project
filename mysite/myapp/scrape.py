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
    try:
        return get_shared_data(username)['entry_data']['ProfilePage'][0]['graphql']['user']['id']
    except:
        return None

def extractLinks(shared_data):
    if not shared_data:
        return None
    links = []
    try:
        for edge in shared_data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']:
            link = edge['node']['display_url']
            links.append(link)
        return links
    except :
        return None

def getProfilePicture(shared_data):
    return shared_data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']