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

#https://www.hexascholars.com/code-snippet/send-email-with-attachment-using-django-form/
class Mails(models.Model):
    artist = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    email =     models.EmailField(null=True) 
    name =   models.CharField(max_length=1000, null=True)
    content = models.CharField(max_length=20000, null=True)
    document = models.FileField(upload_to='images/', null=True)
    def __str__(self):
        return self.email  
