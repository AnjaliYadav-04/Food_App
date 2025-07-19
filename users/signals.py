from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)#this function is to be called whenever it recieves post_save signals fron the sender who is user
def build_profile(sender,instance,created,**kwargs): 
    #sender:if user register and save himself, then sender will notify , 
    # created: it is a boolean value that check if the user is registered or not
    #**kwargs : it include in any other aurguments added to thwe function
    if created:
        Profile.objects.create(user=instance)# it create object 1st

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()