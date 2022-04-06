from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    # picture = CloudinaryField('image')


class Profile(models.Model):
    avatar = models.ImageField(upload_to='image', null=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    name =models.CharField(max_length=50, blank=True)
    bio = models.TextField(null=True)

    
    def __str__(self):
        return self.use

    def save_profile(self):
        self.save()

    def save_profile(self):
        self.save()    
