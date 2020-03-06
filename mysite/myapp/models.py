from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    insta_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    profile_picture = models.CharField(max_length=300, blank=True)
    def __str__(self):
        return "{0} {1} {2}".format(self.first_name, self.last_name, self.insta_name)

class Picture(models.Model):
    picture_url = models.CharField(max_length=300)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.picture_url