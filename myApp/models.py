from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to = 'myImage')
    date = models.DateTimeField(auto_now_add = True)
