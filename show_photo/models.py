from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(AbstractUser):
# #     name = models.CharField(max_length=200, null=True)
# #     # email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)
#     avatar = models.ImageField(null=True, default="avatar.svg")



class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to = '',null=True, default="avatar.svg")
    name = models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Messages(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    message = models.TextField(null=True,blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-update', '-created']
    def __str__(self):
        return self.message[:50]

    


