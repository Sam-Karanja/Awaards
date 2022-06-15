from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field PhoneField

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE, related_name='profile')
    bio= models.TextField(max_length=400, blank= True,)
    name= models.CharField(max_length=120, blank=True)
    profile_pic= models.ImageField(upload_to_'images/',default= 'v1639327874/images/default_drurzc.jpg')
    phone_number=PhoneField(max_length=15, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance, Kwargs):
        instance.save()



class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=300)
    url= models.URLField(max_length=400)
    photo=models.ForeignKey(User, on_delete=models.CASCADE,relate_name="posts")
    upload_date=models.DateTimeField(auto_now_add=True, blank=True)
    technologied_used= models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.title}'


    def delete_post(self):
        self.delete()

    @classmethod
    def search