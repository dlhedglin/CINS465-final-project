from django.db import models
from custom_user.models import MyUser

class Picture(models.Model):
    picture_url = models.CharField(max_length=300)
    artist = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.picture_url
        
#https://www.geeksforgeeks.org/python-uploading-images-in-django/
class static_image(models.Model): 
    artist = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    def __str__(self):
        return "{} {} {}".format(self.artist.first_name, self.artist.last_name, self.img)
